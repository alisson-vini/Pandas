import pandas as pd


# CARREGANDO UMA TABELA

dicionario = {
    "Nome":["Alisson", "Zé", "Maria", "Marcos",],
    "Salário":[3200, 1800, 3000, 4900]
}

tabela = pd.DataFrame(dicionario)
tabela = pd.read_csv("excel.csv", sep=";")


# EXPLORANDO O DATAFRAME

#print(f"{tabela.head()}")         # imprime as 5 primeiras linhas
#print(f"{tabela.info()}")         # mostra tipos de dados e valores nulos
#print(f"{tabela.shape}")          # mostra o formato (linhas, colunas)
#print(f"{tabela.columns}")        # mostra todas as colunas da tabela
#print(f"{tabela.dtypes}")         # mostra o tipo de dados de cada coluna



# ACESSANDO INFORMAÇÕES DA TABELA
#print(tabela["nome"])                                                  # printa uma coluna
#print(tabela[["nome", "plano"]])                                       # printa várias colunas
#print(tabela.iloc[0])                                                  # printa uma linha (linha 0)
#print(tabela.iloc[0,1])                                                # printa uma célula (linha 0, coluna 1)
#print(tabela.iloc[ [0,1,2],[1,4] ])                                    # printa uma multiplas linha e coluna de acordo com o indece
#print(tabela.loc[ [0,1,2],["nome","media de atraso de pagamento"] ])   # printa multiplas linhas e colunas de acordo com o index e o nome da coluna