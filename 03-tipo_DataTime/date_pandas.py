"""

O Pandas possui um tipo especial chamado datetime, usado para armazenar datas. Muitas vezes, é necessário converter uma coluna que está como objeto (object) ou string para o tipo datetime, para podermos trabalhar corretamente com datas.

Isso é importante porque, após a conversão, podemos fazer filtragens e operações baseadas em data, como:

# exemplo de filtro
tabela[(tabela["coluna"].dt.month >= 8) & (tabela["coluna"].dt.year == 2025)]


coluna.dt.month → retorna o mês da data

coluna.dt.year → retorna o ano da data

"""


import pandas as pd
import os

# CARREGA A TABELA
caminho_script = os.path.dirname(__file__)                 # pega o diretorio da pasta atual
caminho_csv = os.path.join(caminho_script, "tabela.csv")   # junta o diretorio atual com o nome do arquivo que contem a tabela
tabela = pd.read_csv(caminho_csv, sep=";")                 # lê o arquivo que contem a tabela e salva como um DataFrame


# ALTERAR O TIPO DA COLUNA PARA DATATIME
print(f"Tipo antes de modificar: {tabela["Data da Compra"].dtypes}")                      # mostra qual o tipo de dado da coluna antes
tabela["Data da Compra"] = pd.to_datetime( tabela["Data da Compra"], format="%d/%m/%Y" )  # altera para o tipo "DataTime"
print("Tipo depois de modificar: {tabela['Data da Compra'].dtypes}\n")                    # mostra qual o tipo de dado da coluna depois da alteração


# CRIANDO FILTROS PARA DATAS
filtro_primeiro_semestre_2025 = (tabela["Data da Compra"].dt.month >= 1) & (tabela["Data da Compra"].dt.month <= 6) & (tabela["Data da Compra"].dt.year == 2025)
filtro_segundo_semestre_2025 = (tabela["Data da Compra"].dt.month >= 7) & (tabela["Data da Compra"].dt.month <= 12) & (tabela["Data da Compra"].dt.year == 2025)


# APLICANDO OS FILTROS
primeiro_semestre_2025 = tabela[filtro_primeiro_semestre_2025].copy() # aplica os filtros criados
segundo_semestre_2025 = tabela[filtro_segundo_semestre_2025].copy()   # aplica os filtros criados

print("Tabela do primeiro semestre de 2025")
print(f"{primeiro_semestre_2025}\n")

print("Tabela do segundo semestre de 2025")
print(f"{segundo_semestre_2025}\n")

print(f'receita total primeiro semestre de 2025: { (primeiro_semestre_2025["Quantidade Comprada"] * primeiro_semestre_2025["Valor Produto"]).sum()}')
print(f'receita total segundo semestre de 2025: { (segundo_semestre_2025["Quantidade Comprada"] * segundo_semestre_2025["Valor Produto"]).sum()}')


# VOLTANDO PARA O FORMATO PADRÃO DE ANTES (caso precise)
tabela["Data da Compra"] = tabela["Data da Compra"].dt.strftime("%d/%m/%Y")
print("\nVoltando ao tipo original")
print(f"{tabela['Data da Compra'].dtypes}")