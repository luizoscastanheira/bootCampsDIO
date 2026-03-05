# Operadores de Associação
# Verificam SE um OBJETO está presente em uma sequencia

# operadores in e not in - Atenção: é case sensitive ao se procurar strings

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)

print("maçã" in frutas)
print("limão" not in frutas)
print("maçã" not in frutas)


print(200 in saques)