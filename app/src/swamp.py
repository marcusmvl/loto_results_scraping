import zipfile
import os
from bs4 import BeautifulSoup
import pandas as pd
import utils

pd.set_option('display.max_columns', 22)
pd.set_option('display.width', 1000)

os.chdir('../..')
CONSTANTS = utils.Defaults()
CURRENT_DATE = CONSTANTS.CURRENT_DATE

path_to_zip_file = CONSTANTS.DIR_PROJECT + '\\raw\\' + CURRENT_DATE + '\megasena_results.zip'
utils.create_folder(directory='temp', name=CURRENT_DATE)
directory_to_extract_to = CONSTANTS.DIR_PROJECT + '\\temp\\' + CURRENT_DATE
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)


path = directory_to_extract_to + '\\d_mega.htm'
soup = BeautifulSoup(open(path),'html.parser')
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

columns_groupby_uf = ['Concurso', 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', '6ª Dezena', 'Arrecadacao_Total', 'Ganhadores_Sena', 'Cidade', 'Rateio_Sena', 'Ganhadores_Quina', 'Rateio_Quina', 'Ganhadores_Quadra', 'Rateio_Quadra', 'Acumulado', 'Valor_Acumulado', 'Estimativa_Prêmio', 'Acumulado_Mega_da_Virada']
columns_groupby_cidade = ['Concurso', 'Data Sorteio', '1ª Dezena', '2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', '6ª Dezena', 'Arrecadacao_Total', 'Ganhadores_Sena', 'Rateio_Sena', 'Ganhadores_Quina', 'Rateio_Quina', 'Ganhadores_Quadra', 'Rateio_Quadra', 'Acumulado', 'Valor_Acumulado', 'Estimativa_Prêmio', 'Acumulado_Mega_da_Virada']

df_cidade_null = df.copy()
df_cidade_null['Cidade'] = df['Cidade'].apply(lambda x: '')
df_uf_group_cidade_null = pd.DataFrame({'UF': df_cidade_null.groupby(columns_groupby_uf, sort=False)['UF']
                                       .apply(','.join).replace(r'\n', '', regex=True)}).reset_index()
df_uf_group_cidade_null.drop('Cidade',  axis=1, inplace=True)
df_com_cidade = df[df['Cidade'].str.contains(pat='[a-zA-Z]', regex=True) == True]

df_cidade_group = pd.DataFrame({'Cidade': df_com_cidade.groupby(columns_groupby_cidade, sort=False)['Cidade']
                               .apply(','.join).replace(r'[^\S\r\n]{2,}', '', regex=True)}).reset_index()


df_final = pd.merge(df_uf_group_cidade_null, df_cidade_group, how="left", on=['Concurso'])
df_final.drop(df_final.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)
df_final.columns = df_final.columns.str.rstrip('_x')

swamp_file_dir = utils.create_folder(directory=CONSTANTS.DIR_PROJECT + '\\swamp', name=CURRENT_DATE)

df_final.to_csv(swamp_file_dir + '\\final.csv', sep='|', index=False)
