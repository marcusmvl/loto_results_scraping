import os
import sys
from bs4 import BeautifulSoup
import pandas as pd
import utils

pd.set_option('display.max_columns', 22)
pd.set_option('display.width', 1000)

os.chdir('..')
CONSTANTS = utils.Defaults()
CURRENT_DATE = CONSTANTS.CURRENT_DATE

try:
    ARG_CMD_INPUT = str(sys.argv[1])
except:
    print('No input argument specifield.\nOnly accepts = [megasena, quina, lotofacil]')

if ARG_CMD_INPUT == 'megasena':
    FILE_NAME = 'd_mega.htm'
    DIR_LAKE = os.path.join(os.getcwd(), 'data', 'lake', 'megasena')
    DIR_SWAMP = os.path.join(os.getcwd(), 'data', 'swamp', 'megasena')
    PATH_TO_FILE = os.path.join(DIR_SWAMP, CURRENT_DATE, FILE_NAME)
    COLUMNS_GROUPBY_UF = ['Concurso', 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena',
                          '6ª Dezena', 'Arrecadacao_Total', 'Ganhadores_Sena', 'Cidade', 'Rateio_Sena',
                          'Ganhadores_Quina', 'Rateio_Quina', 'Ganhadores_Quadra', 'Rateio_Quadra', 'Acumulado',
                          'Valor_Acumulado', 'Estimativa_Prêmio', 'Acumulado_Mega_da_Virada']
    COLUMNS_GROUPBY_CITY = ['Concurso', 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena',
                              '5ª Dezena', '6ª Dezena', 'Arrecadacao_Total', 'Ganhadores_Sena', 'Rateio_Sena',
                              'Ganhadores_Quina', 'Rateio_Quina', 'Ganhadores_Quadra', 'Rateio_Quadra', 'Acumulado',
                              'Valor_Acumulado', 'Estimativa_Prêmio', 'Acumulado_Mega_da_Virada']

elif ARG_CMD_INPUT == 'quina':
    FILE_NAME = 'd_quina.htm'
    DIR_LAKE = os.path.join(os.getcwd(), 'data', 'lake', 'quina')
    DIR_SWAMP = os.path.join(os.getcwd(), 'data', 'swamp', 'quina')
    PATH_TO_FILE = os.path.join(DIR_SWAMP, CURRENT_DATE, FILE_NAME)
    COLUMNS_GROUPBY_UF = ['Concurso', 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena',
                          'Arrecadacao_Total', 'Ganhadores_Quina', 'Cidade', 'Rateio_Quina', 'Ganhadores_Quadra',
                          'Rateio_Quadra', 'Ganhadores_Terno', 'Rateio_Terno',
                          'Ganhadores_Duque', 'Rateio_Duque', 'Acumulado', 'Valor_Acumulado', 'Estimativa_Premio',
                          'Valor_Acumulado_Sorteio_Especial_São_João']
    COLUMNS_GROUPBY_CITY = ['Concurso', 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena',
                          'Arrecadacao_Total', 'Ganhadores_Quina', 'Rateio_Quina', 'Ganhadores_Quadra',
                          'Rateio_Quadra', 'Ganhadores_Terno', 'Rateio_Terno',
                          'Ganhadores_Duque', 'Rateio_Duque', 'Acumulado', 'Valor_Acumulado', 'Estimativa_Premio',
                          'Valor_Acumulado_Sorteio_Especial_São_João']
elif ARG_CMD_INPUT == 'lotofacil':
    FILE_NAME = 'd_lotfac.htm'
    DIR_LAKE = os.path.join(os.getcwd(), 'data', 'lake', 'lotofacil')
    DIR_SWAMP = os.path.join(os.getcwd(), 'data', 'swamp', 'lotofacil')
    PATH_TO_FILE = os.path.join(DIR_SWAMP, CURRENT_DATE, FILE_NAME)
    COLUMNS_GROUPBY_UF = ['Concurso', 'Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7',
                          'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15',
                          'Arrecadacao_Total', 'Ganhadores_15_Números', 'Cidade', 'Ganhadores_14_Números',
                          'Ganhadores_13_Números', 'Ganhadores_12_Números', 'Ganhadores_11_Números',
                          'Valor_Rateio_15_Números', 'Valor_Rateio_14_Números', 'Valor_Rateio_13_Números',
                          'Valor_Rateio_12_Números', 'Valor_Rateio_11_Números', 'Acumulado_15_Números',
                          'Estimativa_Premio', 'Valor_Acumulado_Especial']
    COLUMNS_GROUPBY_CITY = ['Concurso', 'Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7',
                          'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15',
                          'Arrecadacao_Total', 'Ganhadores_15_Números', 'Ganhadores_14_Números',
                          'Ganhadores_13_Números', 'Ganhadores_12_Números', 'Ganhadores_11_Números',
                          'Valor_Rateio_15_Números', 'Valor_Rateio_14_Números', 'Valor_Rateio_13_Números',
                          'Valor_Rateio_12_Números', 'Valor_Rateio_11_Números', 'Acumulado_15_Números',
                          'Estimativa_Premio', 'Valor_Acumulado_Especial']
else:
    print(f'Invalid input = {ARG_CMD_INPUT}\nOnly accepts = [megasena, quina, lotofacil]')

with open(PATH_TO_FILE, 'rb') as f:
    file_read = f.read()
soup = BeautifulSoup(file_read, 'html.parser')
html_table = soup.find_all("table")

html_all_trs = html_table[0].find_all('tr')
html_tr_header = html_all_trs[0]
html_tr_rows = html_all_trs[1:]

headers = [header.get_text() for header in html_tr_header.find_all('th')]
rows = [[cell.get_text() for cell in row.find_all('td')] for row in html_tr_rows]

rowspan = []
for no, tr in enumerate(html_tr_rows):
    for td_no, data in enumerate(tr.find_all('td')):
        if data.has_attr("rowspan"):
            rowspan.append((no, td_no, int(data["rowspan"]), data.get_text()))
if rowspan:
    for i in rowspan:
        for j in range(1, i[2]):
            rows[i[0]+j].insert(i[1], i[3])


df = pd.DataFrame(data=rows, columns=headers)

df_cidade_null = df.copy()
df_cidade_null['Cidade'] = df['Cidade'].apply(lambda x: '')
df_uf_group_cidade_null = pd.DataFrame({'UF': df_cidade_null.groupby(COLUMNS_GROUPBY_UF, sort=False)['UF']
                                       .apply(','.join).replace(r'\n', '', regex=True)}).reset_index()
df_uf_group_cidade_null.drop('Cidade',  axis=1, inplace=True)
df_com_cidade = df[df['Cidade'].str.contains(pat='[a-zA-Z]', regex=True) == True]

df_cidade_group = pd.DataFrame({'Cidade': df_com_cidade.groupby(COLUMNS_GROUPBY_CITY, sort=False)['Cidade']
                               .apply(','.join).replace(r'[^\S\r\n]{2,}', '', regex=True)}).reset_index()


df_final = pd.merge(df_uf_group_cidade_null, df_cidade_group, how="left", on=['Concurso'])
df_final.drop(df_final.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)
df_final.columns = df_final.columns.str.rstrip('_x')

utils.create_folder(directory=DIR_LAKE, name=CURRENT_DATE)
LAKE_FILE_DIR = os.path.join(DIR_LAKE, CURRENT_DATE, 'treated.csv')
df_final.to_csv(LAKE_FILE_DIR, sep='|', index=False)
