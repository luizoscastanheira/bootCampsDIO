## CONJUNTOS - estrutura de dados set - é uma coleção de objetos que NÃO possui objetos 
# repetidos.
# usamos os sets para represtar conjuntos matemáticos OU eliminar itens duplicados 
# de um ITERÁVEL
#
# eu uso chaves {} ou o construtor set()

# com construtor
print(set([1, 1, 3, 4, 3, 6, 7 ]))
print(set("abacaxi"))
print(set(("pálio", "gol", "celta", "pálio")))

# com chaves
linguagens = {" Python", "Java", "C#", "Python"}
print(linguagens)

## ACessando dados - Conjuntos em Python NÃO suportam idenxação e nem fatiamento!!!!
# para cessar seru valores é necessa'rio CONVERTER o conjunto para lista

numeros = {1, 1, 3, 4, 3, 6, 7}
print(numeros)
#print(numeros[2]) ## AQUI Dá um erro, descomento para ver como é

# CONVERTENDO um conjunto(set) em uma lista(list)
lista_de_numeros = list(numeros)

print(lista_de_numeros)
print(lista_de_numeros[2])

# ITERANDO
for numero in numeros:
    print(numero)

for indice, numero in enumerate(numeros):
    print(f"{indice} : {numero}")

## MÉTODOS da classe set - muito útil pois serve para o trabalho de conjuntos matemáticos 
# que vimos na escola

conjunto_a = {1, 2, 3}
conjunto_b = {2, 1, 3, 4, 5, 6}
conjunto_c = {10, 0}

# {}.union()
conjunto_uniao = conjunto_a.union(conjunto_b)
print(conjunto_uniao)

# {}.intersection()
conjunto_intercessao = conjunto_a.intersection(conjunto_b)
print(conjunto_intercessao)

# {}.diffence()
print(conjunto_a.difference(conjunto_b)) # o que tem no a que não tem no b
print(conjunto_b.difference(conjunto_a)) # o que tem no b que não tem no a

# {}.symmetric_difference() - já retorna de uma vez as diferenças entre os dois conjunto em 
# um conjunto só
conjunto_simetrico = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_simetrico)

# {}.issubset() - verifica  se um conjunto é subconjunto de outro ( o está contido em)
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# {}.issuperset() - verifica  se um conjunto contem outro (o contem )
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# {}.isdisjoint() - operação de conjunto disjunto verificam SE todos os elementos de um 
# conjunto NÃO estão no outro ou seja se os conjunto se tocam ou não se tocam
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_c))

# {}.add() - adicona um elemento ao set
sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

# {}.clear() - limpa o set
sorteio.clear()
print(sorteio)

# {}.copy() - copia o set
sorteio = {1,23}
sorteio.copy()
print(sorteio)

# {}.discard() - descarta um elemento do set
conjunto_b = {2, 1, 3, 4, 5, 6}
conjunto_b.discard(6)
conjunto_b.discard(45) # se o valor nÃo existe ele não dá erro, só ignora
print(conjunto_b)

# {}.pop() - descarta um elemento do inicio do set
numeros = set(range(10))
print(numeros)

numeros.pop()
numeros.pop()

print(numeros)

# {}.remove() - removo um elemento passado como argumento
numeros.remove(5)
print(numeros)

#numeros.remove(45) # se o elemento nào existe dá erro
print(numeros)

# {}.len() - verifica o tamanho do conjunto, seu numero de elementos
print(len(numeros))

# {}.in() - verifica se um elemento passado como argumento está no set
print(1 in numeros)
print(7 in numeros)
