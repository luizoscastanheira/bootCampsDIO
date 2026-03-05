# Variáveis e Constantes

## Boas práticas
# Os nomes devem seguir o snake_case: exemplo: taxa_de_juros, tamanho_da_peca
# EScolha nomes sugestivos
# Nomeda constantes deve estar em MAIUSCULO

# Variáveis
saldo_total = 1000
print(saldo_total)
saque = 100
saldo_total-= saque
print(saldo_total)
print(type(saldo_total))

saque = 123.45
saldo_total -= saque
print(saldo_total)

print(type(saldo_total))

# Constantes
# Em Python NÃO há palavra reservada para definir constantes
# Crio o nome da constante com LETRAS maiúsculas - é uma convenção que indica
# constante e não uma variável e eu NÃO deve tentar mudar o valor dela

AMOUNT = 30.2
print(AMOUNT)

ESTADOS_SUDESTE = ["RJ", "SP", "MG", "ES"]

print(ESTADOS_SUDESTE)

for estados in ESTADOS_SUDESTE:
    print(estados)
    if (estados == "RJ"):
        print(f"eu moro nesse: {estados}")
