## O Fatiamento é uma técnica utilziada para retornar sbstrings (partes da string original)
# informando inicio(start), fim(stop) e passo (step)
# [start:stop[,step]]

nome = "Rosicléia Moraes Silva Castanheira"

print(nome[0]) # apenas o índice 0

# sem indicar o start(antes dos :) o índice 0 é o padrão e indicando o stop após os : 
# sempre no padrão n - 1 LEMBRA DISSO?

print(nome[:11]) 

# usando o start: mas sem passar o stop
print(nome[10:])

# usando start:stop
print(nome[10:16])

# usando star:stop:step
print(nome[10:16:2])

# exibindo tudo - retorna uma copia da string
print(nome[:])

# exibindo em ordem reversa - é o truque do ESPELHAMENTO da string
print(nome[::-1])
