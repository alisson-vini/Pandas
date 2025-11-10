import pandas as pd
import os


caminho_script = os.path.dirname(__file__)
caminho_csv = os.path.join(caminho_script, "tabela.csv")
tabela = pd.read_csv(caminho_csv, sep=";")

# FILTRO JUNTO COM A TABELA

# print(tabela[ tabela["nome"] == "Alisson" ]) # todas as linhas que tem "Alisson" na coluna "nome"
# print(tabela[ (tabela["pais"] == "Brasil") & (tabela["idade"] >= 18) ]) # todos que moram no Brasil e tem idade >= 18
# print(tabela[ tabela["nome"].str.contains("^A", case=False, na=False) ]) # todos que tem nomes que começam com a letra A


# CRIAÇÃO DE MULTIPLOS FILTROS QUE PODEM SER USADOS SEPARADAMENTE (mascaras booleanas)

filtro_maior_idade = tabela["idade"] >= 18 # quem tem idade >= a 18 anos
filtro_morar_canada = tabela["pais"].str.contains("Canadá", case=False, na=False) # quem mora no canadá
filtro_sexo = tabela["sexo"] == "M" # quem é homem

# APLICANDO FILTROS CRIADOS
print(tabela[ 
    filtro_maior_idade & filtro_morar_canada & ~filtro_sexo
 ])