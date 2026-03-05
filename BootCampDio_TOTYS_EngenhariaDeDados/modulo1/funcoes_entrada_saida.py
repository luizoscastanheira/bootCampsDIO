# FunçoeS de entra e saida - ler dados de entrada do usuário, precessar e devolver na saida

# função input é uma funçao built-in e recebe na netrada padrão um argumento tipo string que é exibido na tela

nome = input("Qual é seu nome: ")
# função print - uma função built-in que exibe dados na saia padrão a tela
# recebe um argumento obrigatorio do tipo varargs de objetos
# pode trabalhar com 4 argumentos opcionais (sep, end, file, flush)
# TODOS os objetos são convertidos em string e separado por sep e terminados por end
print(nome, end="... ;-)")

## outros exemplos de print
nome = "Rosicléia"
sobrenome = "Castanheira"
print(nome, sobrenome)
print(nome, sobrenome, end="...\n ;-) \n")
print(nome, sobrenome, sep="#")

## CAlculando
numero1 = input("entre com o primeiro numero: ")
numero2 = input("entre com o segundo numero: ")
print(numero1 + numero2) ## CONCATENOU
print(float(numero1) + float(numero2))