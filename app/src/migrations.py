import os
import utils

os.chdir('../..')
CONSTANTS = utils.Defaults()

utils.create_folder(directory=CONSTANTS.DIR_PROJECT, name='log')
utils.create_folder(directory=CONSTANTS.DIR_PROJECT, name='temp')
utils.create_folder(directory=CONSTANTS.DIR_PROJECT, name='raw')
utils.create_folder(directory=CONSTANTS.DIR_PROJECT, name='swamp')




