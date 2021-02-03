import os
import time
impot datetime
import logging
import requests
from bs4 import BeautifulSoup

URL_MEGA_SENA_LANDING = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena'
HTML_A_CLASS_DOWNLOAD_ZIPS = 'title zeta'
HTTP_CODE_SUCCESS_INFO = list(range(100, 200))
HTTP_CODE_SUCCESS = list(range(200, 300))
HTTP_CODE_CLIENT_ERROR = list(range(400, 500))
HTTP_CODE_SERVER_ERROR = list(range(500, 600))
DATETIME_FORMAT = '%Y-%m-%d'

current_date = datetime.datetime.fromtimestamp(time.time()).strftime(DATETIME_FORMAT)
logging.basicConfig(filename='mega_sena_results_' + current_date + '.log', filemode='w', level=logging.DEBUG)


def scraping(page_requested):
    soup = BeautifulSoup(page_requested.content, 'html.parser')
    htlm_as = soup.find_all('a', class_=HTML_A_CLASS_DOWNLOAD_ZIPS, href=True)
    url_zip_download_links = [a['href'] for a in htlm_as if a['href'][-4:] == '.zip']
    return url_zip_download_links


def downlod_zip_content(url):
    content = requests.get(url)
    if content.status_code in HTTP_CODE_SUCCESS:
        donwload_dir = create_folder()
        with open(donwload_dir + '/' + 'megasena_results.zip', 'wb') as zip_file:
            zip_file.write(content.content)
            logging.info('Zip file downloaded.')
        return True
    else:
        logging.error(f'Zip file not downloaded, status code={content.satus_code}')
        return False


def create_folder(dir=os.getcwd(), name=current_date):
    directory = dir + '/' + name
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f'Directory created: {directory}')
        return directory

    logging.info('Directory not created.')
    return directory


if __name__ == '__main__':
    logging.info(f'MEGA SENA LANDING PAGE:{URL_MEGA_SENA_LANDING}')
    try:
        page = requests.get(URL_MEGA_SENA_LANDING)
    except NameError:
        logging.error(f'Cound not connect to: {URL_MEGA_SENA_LANDING}')
        print('Script stopped.')
    logging.info(f'Status code response: {page.status_code}')

    if page.status_code in HTTP_CODE_SUCCESS or page.status_code in HTTP_CODE_SUCCESS_INFO:
        logging.info('Site accessed')
        url_zip_download_contents = scraping(page)
        if not url_zip_download_contents:
            logging.error(f'HTML Elements not found, check HTML_A_CLASS_DOWNLOAD_ZIPS={HTML_A_CLASS_DOWNLOAD_ZIPS}')
            quit()
        else:
            logging.info(f'Downloading Zip Content from: {url_zip_download_contents[0]}')
            downlod_zip_content(url_zip_download_contents[0])
    elif page.status_code in HTTP_CODE_CLIENT_ERROR or page.status_code in HTTP_CODE_SERVER_ERROR:
        logging.info('Site not accessed, check URL or Internet Connection')

