import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações de Dados Reais
nomes = ["Ricardo Almeida", "Beatriz Souza", "Carlos Silva", "Mariana Costa", "Fernanda Oliveira", "João Pedro", "Ana Paula", "Lucas Ferreira", "Juliana Mendes", "Roberto Rocha"]
sobrenomes = ["Santos", "Lima", "Mendes", "Rocha", "Antunes", "Barbosa", "Vitorio", "Martins", "Machado", "Cavalcante"]

produtos_dados = [
    ("Phone 15 Pro", 8499.00, "Eletrônicos"),
    ("Fritadeira", 389.90, "Eletrodomésticos"),
    ("Camisa Polo", 450.00, "Vestuário"),
    ("Smart TV", 2600.00, "Eletrônicos"),
    ("Jogo de Panelas", 299.00, "Cozinha"),
    ("Notebook", 3450.00, "Informática"),
    ("Têni", 549.90, "Calçados"),
    ("Monitor", 950.00, "Informática"),
    ("Toalha", 85.00, "Cama Mesa e Banho"),
    ("Cafeteira", 499.00, "Eletrodomésticos"),
    ("Console", 3799.00, "Eletrônicos"),
    ("Mouse", 580.00, "Informática"),
    ("Micro", 750.00, "Eletrodomésticos"),
    ("Bloco de notas eletrico", 799.00, "Eletrônicos")
]

data_inicio = datetime(2025, 1, 1)
registros = []

for i in range(1, 1001):
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    prod, valor, setor = random.choice(produtos_dados)
    qtd = random.randint(1, 3)
    data_venda = data_inicio + timedelta(days=random.randint(0, 450))
    
    registros.append({
        "id": i,
        "data_aq": data_venda.strftime("%Y-%m-%d"),
        "cliente": nome_completo,
        "produto": prod,
        "quantidade": qtd,
        "valor_un": valor,
        "total": round(qtd * valor, 2),
        "setor": setor
    })

df = pd.DataFrame(registros)
df.to_csv("vendas_loja_1000.csv", index=False, encoding="utf-8")
print("Arquivo 'vendas_loja_1000.csv' gerado com sucesso.")
