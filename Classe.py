class Banco:
    
    def __init__(self, nome, cnpj, contas):
        self.nome = nome
        self.cnpj = cnpj
        self.contas = {}

    def criar_conta(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.contas[self.id] = [self.nome, self.cpf]
        
    def sacar(self, conta, valor):
        pass