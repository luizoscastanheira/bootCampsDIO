import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações de Dados Reais
nomes = ["Ricardo Almeida", "Beatriz Souza", "Carlos Silva", "Mariana Costa", "Fernanda Oliveira", "João Pedro", "Ana Paula", "Lucas Ferreira", "Juliana Mendes", "Roberto Rocha"]
sobrenomes = ["Santos", "Lima", "Mendes", "Rocha", "Antunes", "Barbosa", "Vitorio", "Martins", "Machado", "Cavalcante"]

produtos_dados = [
    ("iPhone 15 Pro Max", 8499.00, "Eletrônicos"),
    ("Fritadeira Air Fryer Mondial", 389.90, "Eletrodomésticos"),
    ("Camisa Polo Lacoste", 450.00, "Vestuário"),
    ("Smart TV LG 55 4K", 2600.00, "Eletrônicos"),
    ("Jogo de Panelas Tramontina", 299.00, "Cozinha"),
    ("Notebook Dell Inspiron 15", 3450.00, "Informática"),
    ("Tênis Nike Air Max", 549.90, "Calçados"),
    ("Monitor Gamer AOC 24", 950.00, "Informática"),
    ("Toalha Buddemeyer", 85.00, "Cama Mesa e Banho"),
    ("Cafeteira Nespresso", 499.00, "Eletrodomésticos"),
    ("Console PlayStation 5", 3799.00, "Eletrônicos"),
    ("Mouse Logitech MX Master", 580.00, "Informática"),
    ("Micro-ondas Brastemp 32L", 750.00, "Eletrodomésticos"),
    ("Kindle Paperwhite 16GB", 799.00, "Eletrônicos")
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