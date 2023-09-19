class Banco:
    
    def __init__(self, nome, cnpj, contas):
        self.nome = nome
        self.cnpj = cnpj
        self.contas = {}

    def criar_conta(self, id, nome, cpf, saldo_inicial):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.saldo_inicial = 0
        self.contas[self.id] = [self.nome, self.cpf]
        
    def sacar(self, conta, valor):
        self.conta = conta
    
        if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print("Seu saque foi realizado com Sucesso!.")

        else:
            print("Você não tem saldo suficiente na conta para que você realize o saque.")

    def depositar(self, conta, valor):
        self.conta = conta

        if valor > 0:
            self.saldo += valor
            print("Seu depósito foi realizado com Sucesso!.")

        else:
            print("O valor minimo de deposito para a conta é a cima de 0, por favor digite o número novamente para depositar.")