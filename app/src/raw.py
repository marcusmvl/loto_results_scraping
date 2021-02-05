import sys
import utils
import logging
import requests
from bs4 import BeautifulSoup

URL_MEGA_SENA_LANDING = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena'
HTML_A_CLASS_DOWNLOAD_ZIPS = 'title zeta'
HTTP_CODE_SUCCESS_INFO = list(range(100, 200))
HTTP_CODE_SUCCESS = list(range(200, 300))
HTTP_CODE_CLIENT_ERROR = list(range(400, 500))
HTTP_CODE_SERVER_ERROR = list(range(500, 600))
CONSTANTS = utils.Defaults()

logging.basicConfig(filename='log\\mega_sena_results_' + CONSTANTS.CURRENT_DATE + '.log', filemode='w', level=logging.DEBUG)
utils.create_folder(directory=CONSTANTS.DIR_PROJECT + '\\raw', name=CONSTANTS.CURRENT_DATE)


def scraping(page_requested):
    """find in Download section from Caixa Mega sena results page and return URLs with .zip content"""
    soup = BeautifulSoup(page_requested.content, 'html.parser')
    htlm_as = soup.find_all('a', class_=HTML_A_CLASS_DOWNLOAD_ZIPS, href=True)
    url_zip_download_links = [a['href'] for a in htlm_as if a['href'][-4:] == '.zip']
    return url_zip_download_links


def downlod_zip_content(url):
    """download zip content from URL and saves in current directory"""
    content = requests.get(url)
    if content.status_code in HTTP_CODE_SUCCESS:
        with open(CONSTANTS.DIR_PROJECT + '\\raw\\' + CONSTANTS.CURRENT_DATE + '\\megasena_results.zip', 'wb') as zip_file:
            zip_file.write(content.content)
            logging.info('Zip file downloaded.')
        return True
    logging.error(f'Zip file not downloaded, status code={content.satus_code}')
    return False


if __name__ == '__main__':
    logging.info(f'MEGA SENA LANDING PAGE:{URL_MEGA_SENA_LANDING}')
    try:
        page = requests.get(URL_MEGA_SENA_LANDING)
    except NameError:
        logging.error(f'Cound not connect to: {URL_MEGA_SENA_LANDING}')
        print('Script stopped.')
        sys.exit()
    logging.info(f'Status code response: {page.status_code}')

    if page.status_code in HTTP_CODE_SUCCESS or page.status_code in HTTP_CODE_SUCCESS_INFO:
        logging.info('Site accessed')
        url_zip_download_contents = scraping(page)
        if not url_zip_download_contents:
            logging.error(f'HTML Elements not found, check HTML_A_CLASS_DOWNLOAD_ZIPS={HTML_A_CLASS_DOWNLOAD_ZIPS}')
            sys.exit()
        else:
            #use index 0 for results in draw order or 1 for asceding order
            logging.info(f'Downloading Zip Content from: {url_zip_download_contents[0]}')
            downlod_zip_content(url_zip_download_contents[0])
    elif page.status_code in HTTP_CODE_CLIENT_ERROR or page.status_code in HTTP_CODE_SERVER_ERROR:
        logging.info('Site not accessed, check URL or Internet Connection')
