# Identação
# ajuda na manutenção e legibilidade do seu código não serve apenas para estetica
#
# No Python a identação serve para identificar e determinar onde inicia e termina um bloco de comando
# não se usa {} para fazer essas marcas.
#
# no Python existe a convensão de usar 4 espaços em branco por nível de identação


def soma(num1, num2):
    return num1 + num2
print(soma(5, 15))


### o Teste abaixo é meu, nada a ver com aula


class Conta:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def sacar(self, valor: float) -> None:
        if self.saldo >= valor:
            self.saldo -= valor

# Criando uma conta com saldo inicial
conta = Conta(1000.00)

# Fazendo um saque
conta.sacar(500.78)

# Imprimindo saldo atualizado
print(conta.saldo)
