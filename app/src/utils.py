import os
import time
import datetime
import logging

os.chdir('../..')

class Defaults:
    DATETIME_FORMAT = '%Y-%m-%d'
    CURRENT_DATE = datetime.datetime.fromtimestamp(time.time()).strftime(DATETIME_FORMAT)
    LOGGING_LEVE = 'logging.DEBUG'
    LOGGING_NAME = CURRENT_DATE + '.log'
    DIR_PROJECT = os.getcwd()


def create_folder(directory=Defaults(), name=Defaults().CURRENT_DATE):
    """create a new folder (if not existis) with a name pattern directory/name"""
    directory = directory + '\\' + name
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f'Directory created: {directory}')
        return directory

    logging.info('Directory not created.')
    return directory
