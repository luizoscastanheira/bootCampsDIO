## Dicionários - São estruturas de dados, um tipo de ados NATIVO no python que se organizam 
# no padrão chave:valor, # assim com se vê no formato JSON (MAS NÃO são amesma coisa). 
# O JSON é um formato de # intercambio de dados tipo texto (string), enquanto um dicionário 
# é um OBJETO vivo na memória.

# AtENÇÃO: dicionários podem conter outros dicionários

# Criando um dicionário simples
pessoa = {"nome":"Rosicléia", "idade":"47", "estado_civil":"casada"}
print(pessoa)

print()
# Acesso aos dados
print(pessoa["nome"])
print(pessoa["idade"])

print()

pessoa["nome"] = "Rosi"
print(pessoa)


print()
# iterando de forma simples
for chave in pessoa:
    print(chave, pessoa[chave])

print()
# iterando com ajuda de um método
for chave, valor in pessoa.items():
    print(chave, valor)

print()
# Criando um dicionário de forma simples mas com uso de construtor
outra_pessoa = dict(nome="Guilherme", idade="47", estado_civil="solteiro")
print(outra_pessoa)

# iterando de forma simples
for chave in outra_pessoa:
    print(chave, outra_pessoa[chave])

# iterando com ajuda de um método
for chave, valor in outra_pessoa.items():
    print(chave, valor)

print()
## Um dicionário um pouco mais complexo 
#  AtENÇÃO: dicionários podem conter outros dicionários
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos)
print()
print(contatos["chappie@gmail.com"])
print(contatos["chappie@gmail.com"]["nome"])

# iterando
for chave in contatos:
    print(chave, contatos[chave])

print()

for chave, valor in contatos.items():
    print(chave, valor)

## Métodos da classe dict

# {}.clear() - limpa, apaga o conteudo do dicionário
#contatos.clear()
print(contatos)

# {}.copy() - copia o conteudo de um dicionário
terceira_pessoa = pessoa.copy()
print(terceira_pessoa)

nova_base = contatos.copy()
print(nova_base)
print(contatos is nova_base)

# {}.fromkeys() - cria  chaves passando se uma lista e é usado em duas cituações:
# 1 - voce quer criar as chaves MAS não quer ainda inserir valor, como valor entra o none automáticamente
# dict.fromkeys(["nome", "telefone"]) # vira {"nome":"none", "telefone":"none"}
#
# 2 - você quer criar as chaver e colocar um valor padrão nelas
# dict.fromkeys(["nome", "telefone"], "vazio") # vira {"nome":"vazio", "telefone":"vazio"}

dicionario1 = dict.fromkeys(["nome", "telefone"])
dicionario2 = dict.fromkeys(["nome", "telefone"],"esta_vazio")
print(dicionario1)
print(dicionario2)

# {}.get() - outra forma de acessar valores no dicionário

#print(contatos["chave"]) # isso dá erro poisa chave não existe

# se não tenho certeza de que uma chave existe no dicionário eu uso o get
# primeira forma
print(contatos.get("chave")) # o retorno é None se a chave não existe
print(contatos.get("guilherme@gmail.com")) # se a chave existe é retornado o valor

# segunda forma - posso passar um segundo argumneto que seria um valor default caso a chave 
# não seja encontrada
print(contatos.get("chave", "A chave solicitada não existe.")) # retorna uma mensagem se chave não existe
print(contatos.get("chave", {})) # retorna um dicionário vazio se chave não existe
print(contatos.get("guilherme@gmail.com", {}))

# {}.items() - retorna uma lsita de tuplas a partir do dicionário, util para iterar com o for
for chave, valor in contatos.items():
    print(chave, valor)

print()    
# note a diferença ente as duas formas de usar o .items()
print(contatos.items())

print()
# {}.keys() - retorna APENAS as chaves do dicionário, util para saber quais são 
# extamente as chaves () - o nome de cada chave e NÃO o seu conteúdo
print(contatos.keys())
chaves = contatos.keys()
print(chaves)

# iterando e caturando as chaves em separado
for chave in contatos.keys():
    print(chave)

print()
# {}.pop() - remove uma chave do dicionário
resultado = contatos.pop("guilherme@gmail.com")
print(resultado)
print(contatos)

print()
#resultado = contatos.pop("guilherme@gmail.com") # se tentar remover um chave que não existe dá erro
#print(resultado)
resultado = contatos.pop("guilherme@gmail.com", "Chave não encontrada")
print(resultado)

print()
# {}.popintem() - remove os itens na sequencia e gera um erro se o dicionário "esvaziar"
print(contatos)
contatos.popitem()
contatos.popitem()
print()
print(contatos)

# Mais exemplos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

pessoa = {"nome":"Rosicléia", "idade":"47", "estado_civil":"casada"}

# {}.setdefault() permite adioncar um valor caso ele não exista
print(pessoa)
pessoa.setdefault("habilitacao", True)
print(pessoa)

for chave, valor in pessoa.items():
    print(chave, valor)

print()
# {}.update() - atualiza nossa dicionário com outro dicionário
# se eu fizer um update com uma chave que já existe ele atualziao o valor da chave
print(contatos)
print(pessoa)

print()

contatos.update({"guilherme@gmail.com":{"nome":"Gui"}})
print(contatos)
contatos.update({"thelosc@gmail.com":{"nome":"Luiz Otavio", "telefone":"456-987"}})
print(contatos)

print()
for chave, valor in contatos.items():
    print(chave, valor)

print()
# {}.values() - retorna só os valores, funciona análogo ao keys
print(contatos.values())
print()
# iterando e caturando as chaves em separado
for valores in contatos.values():
    print(valores)
else:
    print(f"O dicionário contatos possui {len(contatos)} itens.")

print()
# método in - uma forma mais elegante de saber se uma chave existe ou não no dicionário
print("thelosc@uol.com" in contatos) # se não existe retorna False
print("guilherme@gmail.com" in contatos) # se existe retorna True
# verificando se uma chave existe no dicionário interno
print("nome" in contatos["guilherme@gmail.com"])
print("telefone" in contatos["guilherme@gmail.com"])

print()
# del - recebe um objeto e o remove do dicionário
# removendo o telefone de um objeto do dicionário
del contatos["melaine@gmail.com"]["telefone"]
print(contatos)

print()
# removendo um item completo
del contatos["giovanna@gmail.com"]
print(contatos)

print()
# removendo o dicionário inteiro descomente abaixo e veja o que acontece
# del contatos 
print(contatos)
