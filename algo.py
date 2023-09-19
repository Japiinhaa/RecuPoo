from Classe import *
import os


def main(opcoes):


    contaid = 000


    match opcoes:
        case 1:
            os.system('pause')
            print('Você selecionou a opção de Criar uma conta!')
            contaid += 1
            id = contaid
            nome = input('Nome: ')
            cpf = int(input('CPF: '))
            Banco.criar_conta(id, nome, cpf)
            os.system("cls")
        case 2:
            os.system('pause')
            print('Você selecionou a opção de Sacar!')
            valor = int(input('Digite o valor desejado à sacar > '))
            Banco.sacar(valor)
            os.system("cls")
        case 3:
            os.system('pause')
            print('Você selecionou a opção de Depositar!')
            valor = int(input('Digite o valor desejado à ser depositado > '))
            Banco.depositar(valor)
            os.system("cls")
        case 4:
            os.system('pause')
            os.system("cls")
            print('Você selecionou a opção de Transferir!')
            Banco.transferir()
        case 5:
            os.system('pause')
            os.system("cls")
            print('Você selecionou a opição de Verificar Saldo')
            Banco.saldo()
        case _:
            print('Opção inválida!')

