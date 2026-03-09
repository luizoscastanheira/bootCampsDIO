## Trabalhando com multiplas linhas ao exibir uma string - ou strings triplas - 
# São definidas inforamdno 3 aspas simples ou duplas DURANTE a ATRIBUIÇÃO
# Elas podem ocupar várias linhas de código e todos os espaços em branco são incluídos n string final

nome = "Guilherme"

mensagem = f"""
    Olá, meu nome é {nome},
EStou estudando Python.
       Essa mensgaem tem diferentes recuos."""

print(mensagem)

# Exemplo

print("""
================= MENU ==================
      
      1 - Depositar
      2 - Sacar
      3 - Sair

=========================================
""")