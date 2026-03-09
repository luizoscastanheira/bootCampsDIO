# A manipulação de strings é algum muito comum e até simples no Python
# Um String é um objeto iteravel, ou seja cada posição que contenha algum
#  carater ou espaço podeser verificado, alterado, dividido, concatenado e etc

# Métodos úteis da classe string

## String e fatiamento e interpolação de valores de variáveis

curso = "pYtHon é mUIto Bom"

# Maiúscula
print(curso.upper())

# Minúscula
print(curso.lower())

# Titulo ou Capitulando
print(curso.title())

print()
print()

## Eliminando espaços em branco
print("Eliminando espaços em branco")
curso = "      Python   "
print(curso)

print(curso.strip()) # retira os espaços em branco da esquerda e da direita

print(curso.lstrip()) # retira os espaços em branco da esquerda

print(curso.rstrip()) # retira os espaços em branco da direita

## Junções e cetralização de string

curso = "Python"

print(curso.center(50,"+"))
print(curso.center(50))

print(".".join(curso)) # join funciona com todo tipo de iterável - ele ITERA a variável - estude a saida paa entender

