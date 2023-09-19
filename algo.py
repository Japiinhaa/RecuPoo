from Classe import *
import os


def criar_conta(self, nome, cpf):
    nome = input('informe seu nome: ')
    cpf = input('informe seu CPF: ')

    def sacar(self, conta, valor):
        self.conta = conta
        self.valor = valor

    def depositar(self, conta, valor):
        pass

    def transferir(self, origem, destino, valor):
        pass

    def saldo(self, conta):
        pass



def main(opcoes):


    contaid = 000

    
    match opcoes:
        case 1:
            print('Você selecionou a opção de Criar uma conta!')
            ()
            os.system("cls")
        case 2:
            print('Você selecionou a opção de Sacar!')
            ()
            os.system("cls")
        case 3:
            print('Você selecionou a opção de Depositar!')
            ()
            os.system("cls")
        case 4:
            os.system("cls")
            print('Você selecionou a opção de Transferir!')
            ()
        case 5:
            os.system("cls")
            print('Você selecionou a opição de Verificar Saldo')
            ()
        case _:
            print('Opção inválida!')

