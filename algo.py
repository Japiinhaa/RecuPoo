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

