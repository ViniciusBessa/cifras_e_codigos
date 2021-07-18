from time import sleep

from .codificadores import *
from .decodificadores import *


def codificar_ou_decodificar() -> str:
    print('Codificar ou decodificar\n')
    print('1 - Codificar\n2 - Decodificar')
    escolha: str = input('Digite uma das opções: ')
    print('\n' * 15)
    return escolha


def programa() -> None:
    while True:
        print('Menu inicial\n')
        print('1 - Tap code (Código da batida)')
        print('2 - Código morse')
        print('3 - Cifra de César')
        print('4 - Cifra de Vigenère')
        print('5 - One-time pad (Cifra de uso único)')
        print('6 - Autokey cipher (Cifra de autochave)')
        print('7 - Sair do programa')
        print()
        escolha1: str = input('Digite umas da opções: ')
        print('\n' * 15)

        if escolha1 == '1':
            escolha2 = codificar_ou_decodificar()
            if escolha2 == '1':
                print(cod_tapcode())
            elif escolha2 == '2':
                print(decod_tapcode())

        elif escolha1 == '2':
            escolha2 = codificar_ou_decodificar()
            if escolha2 == '1':
                print(cod_morse())
            elif escolha2 == '2':
                print(decod_morse())

        elif escolha1 == '3':
            escolha2 = codificar_ou_decodificar()
            if escolha2 == '1':
                print(cod_cesar())
            elif escolha2 == '2':
                print(decod_cesar())

        elif escolha1 == '4':
            escolha2 = codificar_ou_decodificar()
            if escolha2 == '1':
                print(cod_vigenere())
            elif escolha2 == '2':
                print(decod_vigenere())

        elif escolha1 == '5':
            escolha2 = codificar_ou_decodificar()
            if escolha2 == '1':
                print(cod_onetimepad())
            elif escolha2 == '2':
                print(decod_onetimepad())

        elif escolha1 == '6':
            escolha2 = codificar_ou_decodificar()
            if escolha2 == '1':
                print(cod_autokey())
            elif escolha2 == '2':
                print(decod_autokey())

        elif escolha1 == '7':
            print('Programa finalizado.')
            break

        else:
            print('Opção inválida.')
        sleep(3)
        print('\n' * 15)
