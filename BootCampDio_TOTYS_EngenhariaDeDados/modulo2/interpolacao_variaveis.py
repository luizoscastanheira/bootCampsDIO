## Interpolação de variáveis
# Temos 3 formas:
# 1 - usando sinal % - NÃO se recomenda mais essa forma no Python 3
# 2 - usando o metodo format
# 3 - usando f strings (Tipo o template strings no JavaScript) - esta é mais usada

# Old style - o uso da %
# %s = valores em string, %d = valores inteiros, %f = valores float
nome = "Rosicléia"
idade = 47
profissao = "Gestora Ambiental"
linguagem = "Python"

print("Olá, eu me chamo %s. Tenho %d anos de idade, trabalho como %s e não entendo de linguagem %s." % (nome, idade, profissao, linguagem))

# Método format
print("Olá, eu me chamo {}. Tenho {} anos de idade, trabalho como {} e não entendo de linguagem {}.".format(nome, idade, profissao, linguagem))

# ABaixo você pode colocar entre {} qual o numero da variável que deve entrar, contando inicio como zero
# observe e note a diferença
print("Olá, eu me chamo {}. Tenho {} anos de idade, trabalho como {} e não entendo de linguagem {}.".format(linguagem, profissao, idade,nome))

print("Olá, eu me chamo {3}. Tenho {2} anos de idade, trabalho como {1} e não entendo de linguagem {0}.".format(linguagem, profissao, idade,nome))

# Outra forma MAS note que está aumentando o código
print("Olá, eu me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e não entendo de linguagem {linguagem}.".format(linguagem = linguagem, profissao = profissao, idade = idade,nome = nome))

# Outra forma MAS com uso de um dicionário
# Criando o dicionário com as informações
pessoa = {
    "nome": "Rosicléia",
    "idade": 47,
    "profissao": "Gestora Ambiental",
    "linguagem": "Python"
}

print("Olá, eu me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e não entendo de linguagem {linguagem}.".format(**pessoa))

# Uso do f-string - a sintaxe usa f"texto texto {nome_da_variavel} texto."

print(f"Olá, eu me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e não entendo de linguagem {linguagem}.")

## DICA - formatando string de valroes decimais com f-string
# }

PI = 3.14159

print(f"O valor de PI é {PI}")
print(f"O valor de PI é {PI:.2f}")
print(f"O valor de PI é {PI:.3f}")
print(f"O valor de PI é {PI:.4f}")

print(f"O valor de PI é {PI:10.2f}")
print(f"O valor de PI é {PI:6.2f}")