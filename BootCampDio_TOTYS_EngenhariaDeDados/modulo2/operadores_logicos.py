# Operadores Lógicos
# São comumente usados com operadores de comparação, para montar um EXPRESSÃO LÓGICA
# o Resultado da expressão lógica é SEMPRE um booleano, True ou False quando um operador de comparção é utilizado
# posso fazer concatenações e gerar grandes expressões

# na condição and para ser True, tudo TEM que ser True
# na condição or para ser True APENAS um tem que ser True

print(True and True ) # dá True
print(True and False) # dá False
print(True or True) # dá True
print(True or False) # dá True
print(False or False) # dá False


saldo = 1000
saque = 250
limite = 200
conta_especial = True

# o que já sabemos e uso normal
print(saldo >= saque)

# criando expressões
# Operador: and(e)
print("Operador and")
print(saldo >= saque and saque <= limite)

# Operador: or(ou)
print("Operador or")
print(saldo >= saque or saque <= limite)

# Operador: not () negação - INVERTE a resposta boolean em uma expressão/comparação
# ou seja, PRIMEIRO é feita a operação que resulta em True ou False DEPOIS é feita uma inversão
# da resposta, se ERA True, VIRA False... Se era False VIRA True -- FIQUE LIGADO

contatos_emergencia = [] # Uma lista  vazia em python resulta em booleano como False


print(not 1000 > 1500) # tem que ser False pois  1000 não é maior que 1500
print(not contatos_emergencia) # uma lista vazia tem que dar False
print(not "saque 1500") # uma string o certo é dar True
print(not "") # uma string vazia - certo é dar False

# precedencia
print()
print("Teste de precedencia sem usar parentesis")
teste_logico = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(teste_logico)

print()
print("Teste de precedencia usando parentesis - facilita a leitura")
teste_logico = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(teste_logico)

# dica: eu posso "quebrar a expressão" atribuindo partes à variáveis e depois comparar as variavéis
# é uma dica de visibilidade para o código

