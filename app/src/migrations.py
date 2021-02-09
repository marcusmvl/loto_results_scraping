import os
import utils

print(os.getcwd())

os.chdir('..')
CONSTANTS = utils.Defaults()

utils.create_folder(directory=os.getcwd(), name='log')
utils.create_folder(directory=os.getcwd(), name='data')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data'), name='raw')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data'), name='swamp')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data'), name='lake')

utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'raw'), name='megasena')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'raw'), name='quina')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'raw'), name='lotofacil')

utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'swamp'), name='megasena')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'swamp'), name='quina')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'swamp'), name='lotofacil')

utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'lake'), name='megasena')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'lake'), name='quina')
utils.create_folder(directory=os.path.join(os.getcwd(), 'data', 'lake'), name='lotofacil')
