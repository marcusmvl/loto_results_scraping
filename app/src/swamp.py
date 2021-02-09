import zipfile
import utils
import sys
import os

os.chdir('..')
CONSTANTS = utils.Defaults()
CURRENT_DATE = CONSTANTS.CURRENT_DATE

try:
    ARG_CMD_INPUT = str(sys.argv[1])
except:
    print('No input argument specifield.\nOnly accepts = [megasena, quina, lotofacil]')

if ARG_CMD_INPUT == 'megasena':
    FILE_NAME = 'megasena_results.zip'
    DIR_RAW = os.path.join(os.getcwd(), 'data', 'raw', 'megasena')
    DIR_SWAMP = os.path.join(os.getcwd(), 'data', 'swamp', 'megasena')
elif ARG_CMD_INPUT == 'quina':
    FILE_NAME = 'quina_results.zip'
    DIR_RAW = os.path.join(os.getcwd(), 'data', 'raw', 'quina')
    DIR_SWAMP = os.path.join(os.getcwd(), 'data', 'swamp', 'quina')
elif ARG_CMD_INPUT == 'lotofacil':
    FILE_NAME = 'lotofacil_results.zip'
    DIR_RAW = os.path.join(os.getcwd(), 'data', 'raw', 'lotofacil')
    DIR_SWAMP = os.path.join(os.getcwd(), 'data', 'swamp', 'lotofacil')
else:
    print(f'Invalid input = {ARG_CMD_INPUT}\nOnly accepts = [megasena, quina, lotofacil]')

path_to_zip_file = os.path.join(DIR_RAW, CURRENT_DATE, FILE_NAME)
utils.create_folder(directory=DIR_SWAMP, name=CURRENT_DATE)
directory_to_extract_to = os.path.join(DIR_SWAMP, CURRENT_DATE)
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
