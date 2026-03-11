# Tuplas - São estruturas de dados similares à listas MAS tem a caracteristica de 
# serem IMUTÁVEIS, ou seja, não se pode alter seu conteúdo após sua criação na memória

# Para criar uma tupla pode faze da seguinte forma:

# Usando o parêntese
estados_br_sudeste = ("MG", "RJ", "ES", "SP")
print(estados_br_sudeste)

# usando un construtor
mercosul = tuple("Brasil")
numeros = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numeros2 = tuple(range(30))


print(mercosul)
print(numeros)
print(numeros2)

for estados in estados_br_sudeste:
    print(estados)

for indice, estados in enumerate(estados_br_sudeste):
    print(f"{indice}: {estados}")

print(estados_br_sudeste[0])
print(estados_br_sudeste[-1])
print(estados_br_sudeste[::-1])

print(estados_br_sudeste.count("MG"))

# Tuplas aninhadas
matriz = (
(1, "a", 2),
("b", 3, 4),
(6, 5, "c"),
)
print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

## FATIAMENTO
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

# ITERANDO 
carros = ("gol", "celta", "palio",)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

## MÉTODOS

# método .count() - conta quantas ocorrencias do argumento passado constam na tupla
cores = ("vermelho", "azul", "verde", "azul",)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

# método .index() - mostra o índice do item passado como argumento
linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

# métido .len() - lista o tamnho da tupla, ou seja, conta seu numero de itens
print(len(linguagens))  # 5
