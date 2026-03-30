## Introdução ao ETL
# Biblioteca Pandas

# importando a biblioteca pandas
import pandas as pd

# importando a biblioteca matplotlib
import matplotlib.pyplot as plt

# Configura para mostrar todos os registros
#pd.set_option("display.max_rows", None)

# Extraindo os dados do arquivi para um variável
df = pd.read_csv("vendas_loja.csv")

# Exibindo o conteudo todo - por padrão p pandas limita a quantidade de linhas mas 
# ou vcê ajusta a configuração com o pd.set_option("display.max_rows", None) OU
# usa o método .to_sting() no dataset
#print(df)
#print(df.to_string())


# Listando que objeto temos para o df
print(f"df é um Objeto da Classe {type(df)}")
print()

# Exibindo as primeiras linhas
print(df.head(n=4))

print()
# Informações - Dá para saber que formato se eocntram os dados de cada coluna, além da 
# quantidade de memória para ler esse conjunto de dados
print(df.info())

print()
# Quantifica quantas linhas e quantas colunas quantificando o volume de informação 
# que estou trabalhando
print(df.shape)

print()
#Alterações nos dados/estutura - Podemos visulizar quais são nossas colunas existentes 
# e até alterar esses nomes bastando passar o novo conjunto de nomes desejados com a MESMA
# quantidade de colunas existente no conjunto original
# 1 - Visualize as colunas
print("Visuzalizando as colunas (cabeçalhos)")
print(df.columns)

print()
# Alterando uma coluna
df.columns = ["id", "data_aq", "cliente", "produto", "QTD", "V.Unitario", "V.Total","setor"]
print(df.columns)
print(df.head(n=4))

print()
## Verificação - para verificar quantos dados faltantes existem em nosso conjunto
print("Verificando com isnull")
print(df.isnull().sum())

print()
# Verifica se o campo tem valor nulo e exibe para cada campo um True ou False
# aqui eu restringi a busca a apenas os 20 primeiros registros
print(df.head(n=20).isnull())

print()
# Verifica valos únicos - No nosso objeto SErie podemos verificar quais os valores 
# únicos existem naquela coluna com o método unique.

# aqui listaria de cada registro
print(df['setor'])

print()
# Aqui vai listar para coluna setor quais os valores estão nela, não repete valor
print(df['setor'].unique())

print()
# AGRUPAMENTOS - a partir desse método simples podemos gerar uma visualização simples e 
# rápida como resultado e sabe o que está acontecendo em nossa base de dados
df["setor"].value_counts().plot(kind='bar')
plt.show()# aqui nós exibimos o resultado com uso da matplotlib

#df["produto"].value_counts().plot(kind='bar')
#plt.show()# aqui nós exibimos o resultado com uso da matplotlib

## Dados ESTATISTICOS - O pandas colabora na exibicão de algumas informações estatisticas a respeito
#  do nosso conjunto de dados e permit que possamosrealizar facilmente uma análise com 
# nosso objeto DataFrame
print(df.describe())
















print()
# graficos simultaneos
#fig, axes = plt.subplots(2, 1, figsize=(8, 10))  # 2 linhas, 1 coluna

#df["setor"].value_counts().plot(kind='bar', ax=axes[0], title="Setor")
#df["produto"].value_counts().plot(kind='bar', ax=axes[1], title="Produto")

#plt.tight_layout()
#plt.show()

