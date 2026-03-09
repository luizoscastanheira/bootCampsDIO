## Estrutura de DADOS

# Listas em Python podem armazenar de maneira sequencial
# qualquer tipo de objeto. Podemos criar listas utilizando o
# construtor list, a função range ou colocando valores separados
# por vírgula dentro de colchetes. Listas são objetos mutáveis,
# portanto podemos alterar seus valores após a criação.

# DICA - uma lista já vem implementada no conceito de PILHA, fique ligado pois isso
# indica como métodos de inserção e remoção de elementos vão trabalhar

frutas = []
print(frutas)
frutas = ["laranja", "maca", "uva"]
print(frutas)

# com uso do construtor list - aqui cada letra vira um elemento
letras = list("python")
# com uso do construtor list MAS usando o range para criar os elementos
numeros = list(range(10))
# Lista com todos os atributos de um carro
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# Exibindo o conteudo da lista de forma simples e direta
print(frutas)
print(letras)
print(numeros)
print(carro)

# ACESSO DIRETO - usando indices - uma lsita permite isso pois é iterável
print(frutas)
print(frutas[0])
print(frutas[-1])
3
print(numeros)
print(numeros[3])
print(numeros[-1])

# LISTA ANINHADA - MUITO USADA na represntação de matriz
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz)
## Atenção aos exemplos abaixo: O que cada um dele captura?
# pense sempre matriz[linha][coluna]
print(matriz[0]) # Capatura a linha 0
print(matriz[0][0]) # captrua o elemento 0 da linha 0

print(matriz[0][-1])
print(matriz[-1][-1])

# Fatiamento da Matriz -e como no fatiamento de string
# fatatiando string
lista = ["p", "y", "t", "h", "o", "n"]
lista[2:]  # ["t", "h", "o", "n"]
lista[:2]  # ["p", "y"]
lista[1:3]  # ["y", "t"]
lista[0:3:2]  # ["p", "t"]
lista[::]  # ["p", "y", "t", "h", "o", "n"]
lista[::-1]  # ["n", "o", "h", "t", "y", "p"]

# fatiando matriz
print(matriz[0:2])
print(matriz[::-1])


# ITERAR LISTA - a forma mais comum é com o for
# iterando de forma padrao
for frutinha in frutas:
    print(frutinha)

# Função enumerate - iterando mas usando o enumerate para descobir os índices - é como o indexOf do javascript
for indice, frutinhas in enumerate(frutas):
    print(f"{indice}: frutinhas")


# COMPREENSAO de lista - muito util pois é uma sintaxe mais curta quando se deseja:
# 1 - criar nova lista com base nos valores de uma lsita existente (filtro)
# 2 - gerar uma nova lsita aplicando alguma modificação nos elementos de uma lista existen (é como o .map() no javascript)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
quadrado = []

# Abaixo um cenário de filtro VERSÃO 1
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# exibinção completa
print(pares)
# iterando
for numero_par in pares:
    print(numero_par)

# Abaixo um cenário de filtro VERSÃO 2 - usando comprehension
# sintaxe:
# variável = [variavel_iteracao for variavel_iteracao in nome_lista if filtro ]

# note que o filtro NÃO é obrigatório
# Sem filtro
listar_pares =[numero for numero in numeros]
print(listar_pares)
# Com filtro
listar_pares = [numero for numero in numeros if numero % 2 == 0]
print(listar_pares)


# Modificando valores - VERSÃO 1
# gerando os numeros ao quadrado
for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

# Modficando valores VERSÃO 2 - comprehension
# elevou ao quadraddo a lista de pares criada no exemplo mais acima
quadrado = [numero ** 2 for numero in pares]
print(quadrado)

## MÉTODOS da CLASSE list
frutas = ["laranja", "maca", "uva"]
print(frutas)
# .append() - adiciona um item ao FINAL da lista
frutas.append("abacate")
print(frutas)

# .clear() - quando quer limpar a lista
frutas.clear()
print(frutas)

# .copy() - cria nova instancia da lista na memoria. uma cópia diferencidada
frutas = ["laranja", "maca", "uva", "maca"]
print(frutas)

frutas_copiadas = frutas.copy()
print(frutas_copiadas)

# verificando se são mesma coisa
print(id(frutas_copiadas), id(frutas))
print(frutas_copiadas is frutas)

# .count(argumento) - usado para contar quantas vezes um objeto passado como argumento existe na lista
print(frutas.count("maca"))

# .extend(argumento) - permite "melhorar append" pois permite que  ao invés de um por um eu adicione uma outra lista inteira à uma lista existente, como um merge de lista
verduras = ["uva", "couve", "alfaçe", "cebolinha"]
print(verduras)

verduras.extend(frutas)
print(verduras)

verduras.extend(["rúcula", "salsa"])
print(verduras)

# .index(argumento) - descobrir a PRIMEIRA ocorrencia de um objeto passo como argumento
print(verduras)
print(verduras.index("salsa"))
print(verduras.index("maca"))

# .pop() - retira o último elemento da lista - segue o padrão pilha
print(verduras)
verduras.pop()
print(verduras)
verduras.pop()
print(verduras)
# se passar o indice do elemento no argumento ele vai direto no elemento e o exclui
verduras.pop(2)
print(verduras)

# .remove(argumento) - remove o elemento da lista passado como argumento e NÃO via indice como no pop
# OBS;: ele remove APENAS  a primeria ocorrencia do elemento
print(verduras) 
verduras.remove("couve")
print(verduras)

# .reverse() - espelha sua lsita
print(verduras)
verduras.reverse()
print(verduras)

# .sort() - ordena nossa lista
print(verduras)
verduras.sort()
print(verduras)
verduras.sort(reverse=True)
print(verduras)
verduras.sort(reverse=False)
print(verduras)

# DICA - ordenando por TAMANHO da palavra (tamanho de cada objeto string da lista)
# aqui fazemos uso de uma função anonima - lambda é uma função anonima
print(verduras)
# da menor palavra paaa maior palavra
verduras.sort(key=lambda x: len(x))
print(verduras)

# da maior palavra para a menor palavra
print(verduras)
verduras.sort(key=lambda x: len(x), reverse=True)
print(verduras)

# .sorted() é uma função built-in
print(verduras)
sorted(verduras)
print(verduras)

# len() = é uma função built-in - mostra o tamanho da lista ou da string
print(len(verduras))
print(f"Nossa lista de verdura possui {len(verduras)} itens.")
