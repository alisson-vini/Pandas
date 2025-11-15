import pandas as pd
import os

# CARREGA A TABELA
caminho_script = os.path.dirname(__file__)                 # pega o diretorio da pasta atual
caminho_csv = os.path.join(caminho_script, "tabela.csv")   # junta o diretorio atual com o nome do arquivo que contem a tabela
tabela = pd.read_csv(caminho_csv, sep=";")                 # lê o arquivo que contem a tabela e salva como um DataFrame

# USANDO O GROUP BY

"""
    O grup by é usado para agrupar uma tabela com base em
    uma coluna e depois aplicar alguma operação nessas mini tabelas
"""

tabela.groupby("estado")      # isso criaria vários "grupinhos", onde cada um deles é formado somente por um tipo tem
                              # somente um estado,N grupos para N = quantidade de valores diferente na tabela


# aplicando uma operação aos grupos criados
soma_mensalidade_estado = tabela.groupby("estado")["mensalidade"].sum()   # cria vários grupos, um para cada cidade e depois soma a coluna valor de cada um desses grupo
print(f"{soma_mensalidade_estado}\n")

media_mensalidade_estado = tabela.groupby("estado")["mensalidade"].mean() # cria vários grupos, um para cada cidade e depois calcula a média de cada um desses grupos
print(f"{media_mensalidade_estado}\n")

quantidade_elementos_estado = tabela.groupby("estado").size()
print(f"{quantidade_elementos_estado}\n")

# OBS: a saída é uma série onde os index são os valores de cada mini grupo (index: PE, RJ, SP; nesse caso)
# então a sintaxe geral do groupby é df.groupby("coluna separadora")["coluna onde vão ser aplicadas as operações"].operação()


# ALGUNS CASOS ESPECIAIS

# várias operações em um groupby
MediaMensalidade_MediaMoradores_estado = tabela.groupby("estado").agg({"mensalidade":"mean", "quantidade moradores":"mean"})
media_soma_mensalidades_estado = tabela.groupby("estado")["mensalidade"].agg(["mean","sum"])
print(f"{MediaMensalidade_MediaMoradores_estado}\n")
print(f"{media_soma_mensalidades_estado}\n")