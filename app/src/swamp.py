import zipfile
import utils
import sys
import os

os.chdir('../..')
CONSTANTS = utils.Defaults()
CURRENT_DATE = CONSTANTS.CURRENT_DATE

try:
    ARG_CMD_INPUT = str(sys.argv[1])
except:
    print('No input argument specifield.\nOnly accepts = [megasena, quina, lotofacil]')

if ARG_CMD_INPUT == 'megasena':
    FILE_NAME = '\megasena_results.zip'
    DIR_RAW = CONSTANTS.DIR_RAW_MEGASENA
    DIR_SWAMP = CONSTANTS.DIR_SWAMP_MEGASENA
elif ARG_CMD_INPUT == 'quina':
    FILE_NAME = '\quina_results.zip'
    DIR_RAW = CONSTANTS.DIR_RAW_QUINA
    DIR_SWAMP = CONSTANTS.DIR_SWAMP_QUINA
elif ARG_CMD_INPUT == 'lotofacil':
    FILE_NAME = '\lotofacil_results.zip'
    DIR_RAW = CONSTANTS.DIR_RAW_LOTOFACIL
    DIR_SWAMP = CONSTANTS.DIR_SWAMP_LOTOFACIL
else:
    print(f'Invalid input = {ARG_CMD_INPUT}\nOnly accepts = [megasena, quina, lotofacil]')

path_to_zip_file = os.getcwd() + DIR_RAW + CURRENT_DATE + FILE_NAME
utils.create_folder(directory=DIR_SWAMP, name=CURRENT_DATE)
directory_to_extract_to = os.getcwd() + DIR_SWAMP + CURRENT_DATE
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)