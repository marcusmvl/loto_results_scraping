import os
import utils

os.chdir('../..')
CONSTANTS = utils.Defaults()

utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_PROJECT, name='log')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_PROJECT, name='data')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_PROJECT + '\\data', name='raw')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_PROJECT + '\\data', name='swamp')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_PROJECT + '\\data', name='lake')

utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_RAW, name='megasena')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_RAW, name='quina')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_RAW, name='lotofacil')

utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_SWAMP, name='megasena')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_SWAMP, name='quina')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_SWAMP, name='lotofacil')

utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_LAKE, name='megasena')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_LAKE, name='quina')
utils.create_folder(directory=os.getcwd() + CONSTANTS.DIR_LAKE, name='lotofacil')