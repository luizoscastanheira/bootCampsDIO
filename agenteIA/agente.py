# Ambiente inicial
ambiente = [5, 12, 7, 3, 18, 1, 34, -1, 666]

# Classe do agente com memória
class Agente:
    def __init__(self, nome):
        self.nome = nome
        self.memoria = []  # lista para armazenar percepções e ações
    
    def perceber(self, ambiente):
        print(f"{self.nome} está observando o ambiente...")
        percepcao = ambiente
        # guarda percepção na memória
        self.memoria.append({"percepcao": percepcao})
        return percepcao
    
    def decidir(self, percepcao):
        print(f"{self.nome} está decidindo...")
        # regra simples: escolher o maior número
        acao = max(percepcao)
        # guarda decisão na memória
        self.memoria[-1]["acao"] = acao
        return acao
    
    def agir(self, acao):
        print(f"{self.nome} escolheu o número {acao} como ação!")
    
    def lembrar(self):
        print(f"\nMemória de {self.nome}:")
        for i, experiencia in enumerate(self.memoria, 1):
            print(f"Experiência {i}: percepção={experiencia['percepcao']} | ação={experiencia['acao']}")

# Instanciando e rodando agente
meu_agente = Agente("Agente_Rosi")

# Ciclo de funcionamento
percepcao = meu_agente.perceber(ambiente)
acao = meu_agente.decidir(percepcao)
meu_agente.agir(acao)

# Consultando memória
meu_agente.lembrar()


# Ciclo de funcionamento
percepcao = meu_agente.perceber(ambiente)
acao = meu_agente.decidir(percepcao)
meu_agente.agir(acao)

# Consultando memória
meu_agente.lembrar()