from Classe import *
from algo import *
import os


if __name__ == '__main__':
    while True:
        try:  
            print("Escolha uma opção: \n 1. Criar uma conta \n 2. Sacar \n 3. Depositar \n 4. Transferir \n 5. Saldo")
            opcoes = int(input('Escolha uma dessa opções:'))
            os.system("cls")
            main(opcoes)

        except Exception as erro:
            os.system("cls")
            print('Erro! Digite apenas números inteiros.')
            