class banco:
    
    def criar_conta(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.conta[self.id] = [self.nome, self.cpf]
        
