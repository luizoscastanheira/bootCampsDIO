## Funções

# definindo, criando as funçes~

# Sem parametros
def exibir_mensagem():
    print("Olá mundo!")

# com parametros
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# com parametro mas já o recebendo como argumento default
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# chamando as funções
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

print()
## Funções que RETORNAM valores - no Python uma função pode retornar mais de um valor

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

print()
## ARgumentos nomeados - podemos usar argumento no formato chave:valor
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
 print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC1234"})
# Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234




## Passando uma função para outra
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a}+ {b}= {resultado}")

exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20