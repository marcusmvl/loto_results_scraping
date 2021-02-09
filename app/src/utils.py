import os
import time
import datetime
import logging

os.chdir('..')


class Defaults:
    DATETIME_FORMAT = '%Y-%m-%d'
    CURRENT_DATE = datetime.datetime.fromtimestamp(time.time()).strftime(DATETIME_FORMAT)
    LOGGING_LEVE = 'logging.DEBUG'
    LOGGING_NAME = CURRENT_DATE + '.log'

    DIR_PROJECT = 'mega_sena_results_scraping'
    DIR_LOG = DIR_PROJECT + 'log'
    DIR_RAW = DIR_PROJECT + 'data\\raw\\'
    DIR_SWAMP = DIR_PROJECT + '\\data\\swamp\\'
    DIR_LAKE = DIR_PROJECT + '\\data\\lake\\'

    DIR_RAW_MEGASENA = DIR_RAW + 'megasena\\'
    DIR_RAW_QUINA = DIR_RAW + 'quina\\'
    DIR_RAW_LOTOFACIL = DIR_RAW + 'lotofacil\\'

    DIR_SWAMP_MEGASENA = DIR_SWAMP + 'megasena\\'
    DIR_SWAMP_QUINA = DIR_SWAMP + 'quina\\'
    DIR_SWAMP_LOTOFACIL = DIR_SWAMP + 'lotofacil\\'

    DIR_LAKE_MEGASENA = DIR_LAKE + 'megasena\\'
    DIR_LAKE_QUINA = DIR_LAKE + 'quina\\'
    DIR_LAKE_LOTOFACIL = DIR_LAKE + 'lotofacil\\'


def create_folder(directory=os.getcwd() + Defaults().DIR_PROJECT, name=Defaults().CURRENT_DATE):
    """create a new folder (if not existis) with a name pattern directory/name"""
    directory = os.path.join(directory, name)
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f'Directory created: {directory}')
        return directory

    logging.info('Directory not created.')
    return directory
