import os
import sys
import utils
import logging
import requests
from bs4 import BeautifulSoup

HTTP_CODE_SUCCESS_INFO = list(range(100, 200))
HTTP_CODE_SUCCESS = list(range(200, 300))
HTTP_CODE_CLIENT_ERROR = list(range(400, 500))
HTTP_CODE_SERVER_ERROR = list(range(500, 600))
CONSTANTS = utils.Defaults()

os.chdir('..')

try:
    ARG_CMD_INPUT = str(sys.argv[1])
except:
    print('No input argument specifield.\nOnly accepts = [megasena, quina, lotofacil]')


if ARG_CMD_INPUT == 'megasena':
    FILE_NAME = 'megasena_results'
    DIR_RAW = os.path.join(os.getcwd(), 'data', 'raw', 'megasena')
    URL_LANDING = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena'
elif ARG_CMD_INPUT == 'quina':
    FILE_NAME = 'quina_results'
    URL_LANDING = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina'
    DIR_RAW = os.path.join(os.getcwd(), 'data', 'raw', 'quina')
elif ARG_CMD_INPUT == 'lotofacil':
    FILE_NAME = 'lotofacil_results'
    URL_LANDING = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil'
    DIR_RAW = os.path.join(os.getcwd(), 'data', 'raw', 'lotofacil')
else:
    print(f'Invalid input = {ARG_CMD_INPUT}\nOnly accepts = [megasena, quina, lotofacil]')

logging.basicConfig(filename=os.path.join(os.getcwd(), 'log', FILE_NAME + CONSTANTS.CURRENT_DATE + '.log'),
                    filemode='w', level=logging.DEBUG)

utils.create_folder(directory=DIR_RAW, name=CONSTANTS.CURRENT_DATE)


def scraping(page_requested):
    """find in Download section from Caixa Mega sena results page and return URLs with .zip content"""
    soup = BeautifulSoup(page_requested.content, 'html.parser')
    htlm_as = soup.find_all('a', href=True)
    url_zip_download_links = [a['href'] for a in htlm_as if a['href'][-4:] == '.zip']
    return url_zip_download_links


def downlod_zip_content(url):
    """download zip content from URL and saves in current directory"""
    requests_data = requests.get(url)
    if requests_data.status_code in HTTP_CODE_SUCCESS:
        with open(os.path.join(os.getcwd(), DIR_RAW, CONSTANTS.CURRENT_DATE, FILE_NAME + '.zip'), 'wb') as zip_file:
            zip_file.write(requests_data.content)
            logging.info('Zip file downloaded.')
        return True
    logging.error(f'Zip file not downloaded, status code={requests_data.satus_code}')
    return False


if __name__ == '__main__':
    logging.info(f'LANDING PAGE:{URL_LANDING}')
    try:
        page = requests.get(URL_LANDING)
    except:
        logging.error(f'Cound not connect to: {URL_LANDING}')
        print('Error: Script stopped, check log file.')
        sys.exit()
    logging.info(f'Status code response: {page.status_code}')

    if page.status_code in HTTP_CODE_SUCCESS or page.status_code in HTTP_CODE_SUCCESS_INFO:
        logging.info('Site accessed')
        url_zip_download_contents = scraping(page)
        if not url_zip_download_contents:
            logging.error(f'HTML Elements not found.')
            sys.exit()
        else:
            logging.info(f'Downloading Zip Content from: {url_zip_download_contents[0]}')
            downlod_zip_content(url_zip_download_contents[0])
    elif page.status_code in HTTP_CODE_CLIENT_ERROR or page.status_code in HTTP_CODE_SERVER_ERROR:
        logging.info('Site not accessed, check URL or Internet Connection')
