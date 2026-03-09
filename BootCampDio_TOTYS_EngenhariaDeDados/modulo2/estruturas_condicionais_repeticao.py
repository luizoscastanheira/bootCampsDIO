# Identação
# ajuda na manutenção e legibilidade do seu código não serve apenas para estetica
#
# No Python a identação serve para identificar e determinar onde inicia e termina um bloco de comando
# não se usa {} para fazer essas marcas.
#
# no Python existe a convensão de usar 4 espaços em branco por nível de identação


def soma(num1, num2) -> float:
    print("Aqui estou dentro do bloco da função soma")
    return num1 + num2

print(soma(5, 15))
print("Aqui estou fora do bloco da função soma")
print("*****************")

### o Teste abaixo é meu, nada a ver com aula

print("## ABaixo é teste objeto, meu teste ##")

class Conta:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def sacar(self, valor: float) -> None:
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"O valor de {valor} foi sacado, o saldo atual é {self.saldo}")

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        print(f"O valor de {valor} foi depositado com sucesso e o novo saldo é {self.saldo}")

# Criando uma conta com saldo inicial
conta = Conta(1000.00)

# Fazendo um saque
conta.sacar(350)

# Imprimindo saldo atualizado
print(conta.saldo)

# Fazendo um deposito
conta.depositar(45.56)

# Imprimindo saldo atualizado
print(conta.saldo)

print()
print("******************************************************")

##############################################################################################
## Estruturas condicionais - permitem que o programa desvie o fluxo de controle e execução
# quando determinadas condições lógicas são atendidas
# isso permite que o programa "tome decisões"

# if / if/else / elif
saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")
if saldo < saque:
    print("Saldo insuficiente!")

saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")
else:
    print("Saldo insuficiente!")

opcao = int(input("Informe uma opção:\n [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print(("Opçao inválida - Saindo do programa..."))
    SystemExit


# if aninhado - basta adicionar "if dentro de if", blocos de if detro de outros
conta_normal = True
conta_universitaria = False
cheque_especial = True

saldo = 2000
saque = 2300
cheque_especial = 450

if conta_normal: # Inicio do Primeiro nivel de if
    if saldo >= saque: # Inicio do segundo nível de if
        print("Saque realizado")
    elif saque <= (saldo + cheque_especial): # Fim do segundo nível de if
        print("Saque com uso do especial")
    else:
        print("Não foi possivel realizar o saque")
elif conta_universitaria: # Fim do Primeiro nivel de if
    if saldo >= saque: # Inicio do segundo nível de if
        print("Saque realizado")
    else: # Fim do segundo nível de if
        print("saldo insuficiente")
else:
    print("Sistema não reconheceu o tipo de conta, procure seu gerente.")


# if ternário - escreve um condição em uma unica linha
# sintaxe:
# parte 1 - retorno SE True
# parte 2 - expressão logica
# parte 3 - retorno SE False

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

## Estruturas de repetição - permitem repetir um bloco de código um 
# certo numero de vezes predeterminada ou até que uma determina condição/expressão lógica determine.

# for e while e a função built-in range

# for - para percorrer um objeto iterável ou quando sabemos o numero de vezes que deve ser executado
texto = input("Informe um texto: \n")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        print() # aqui foi só para quebrar linha 

# é possivel mas não muito comum usar um else no for       


for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        print() # aqui foi só para quebrar linha 
else:
    print("executei no final do laço")

# Enumerar itens: Use enumerate() para obter o índice e o valor simultaneamente.
for indice, valor in enumerate(texto):
    print(indice, valor)


## Função built-in range do python é usada para produzir uma SEQUENCIA de numeros inteiros 
# a  partir de um inicio (inclusivo) para um fim (exclusivo) 
# se usamos range(i,j) temos i, i+1, i+2, i+3, ..., j - 1.
# ele recebe 3 argumentos: stop(obrigatório), start(opcional) e step(opcional)
# OBSERVAÇAO - o range por padrão inicia em 0 - logo um range(10) vai listar de 0 a 9

for numero in range(10):
    print(numero, end=" ")

print(list(range(5))) ## outra forma de usar

# tabuado do 5 - note que usamos start(0), fim(51) e step(5)
for numero in range(0, 51, 5):
    print(numero, end=" ")

print()
print()
contador = 0
for limao in range(1, 11):
    print(limao)
    contador += limao

total_cura = (contador * 2) -10

print(contador)
print(total_cura)


# Estrutura while - repete um bloco várias vezes quando não sabemos o numero exato de 
# execuções

opcao = -1
while opcao != 0:
    opcao = int(input("[1] De Frente \n[2] De Lado \n[0] Sair \n:"))
    if opcao == 1:
        print("Bontando  de Frente")
    elif opcao == 2:
        print("Botando de lado")
    elif opcao == 0:
        print("Saindo :-(")
else:
    print("Obrigado por usar o app")

## Uso do break e do continue
# note que se a condição é True como no exemplo abaixo, temos um loop infinito 
# ate que uma condição de parada seja atingida
# o continue pula uma iteração especificada enquanto o break para a execução na condição especificada

while True:
    opcao = int(input("Digite um número: "))

    if opcao % 2 == 0:
        print(f"O número {opcao} é par. Continuando")
    else:
        print(f"O número {opcao} é impar. Saindo")
        break
else:
    print("Obrigado por usar nosso app par ou impar!")