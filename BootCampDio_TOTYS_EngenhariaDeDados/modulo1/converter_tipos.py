# em alguns caso é necessário converter o tipo contido em uma variável
# exemplo: variável tipo string quecontém um número

# de inteiro para float
# variável declarada com inteiro
preco = 10
print(preco)
# agora a variável preco vai ser convertida quando passamos a variável ao "construtor" float
preco = float(preco)
print(preco)
# outra forma: usadno a divisão pois ao dividir um inteiro por outro valor o resultado é um float
preco = 10 / 2
print(preco)

## Converter flaot para inteiro
# usando o construtor int()
preco = 10.30
print (preco)

preco = int(preco)
print(preco)

# outra forma: cverter por divisão
preco = 10
print(preco)

print(preco / 2) # aqui ainda temo um flot como resultado
print(type(preco / 2))

print(preco // 2) # aqui virou um inteiro
print(type(preco // 2))

# Converter numero para string novamente usamos o construtor str() passando pra ele o valor

preco = 10.50
idade = 28
print(str(preco))
print(str(idade))
print(type(str(idade)))

texto = f"idade {idade}, preco {preco}"
print(texto)

## Converter string para numero
preco = "10.50"
idade = "28"
print(float(preco))
print(int(idade))

## ATNEÇAO - nem sempre é possível converter um tipo para outro
# exemplo
# print(float("python"))