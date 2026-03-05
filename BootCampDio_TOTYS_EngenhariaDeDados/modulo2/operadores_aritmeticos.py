# Operadores Aritméticos

# adição
print(1 + 1)
#subtração
print(5 - 1)
# multiplicação
print(5 * 5)
# divisão
print(12 / 3)
# divisão inteira
print(12 // 3)
# módulo - resto da divisão
print(10 % 3)
# Exponenciação
print(2 ** 3)

## Ordem de precedência: parentesis, expoente, mult e div (quem vier primeiro - da esquerda para direita), soma e subtração (quem vier primeiro - da esquerda para direita)
## Boa prática: Mesmo o Python sabendo da ordem, explicite com parentesis pois visualmente fica melhor para humanos.

print(10 - 5 * 2) # notou? dá 0
print((10 - 5) * 2) # notou? dá 10

print(10 ** 2 * 2)
print(10 ** (2 * 2))

print(10  / 2 * 4)