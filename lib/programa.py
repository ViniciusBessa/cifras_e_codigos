from time import sleep

from .codificadores import *
from .decodificadores import *

# Lista contendo o nome da criptografia e suas funções
opcoes_cripto = [
    ['Cifra de César', cod_cesar, decod_cesar],
    ['Cifra de Vigenère', cod_vigenere, decod_vigenere],
    ['One-time pad (Cifra de uso único)', cod_onetimepad, decod_onetimepad],
    ['Código morse', cod_morse, decod_morse],
    ['Tap code (Código da batida)', cod_tapcode, decod_tapcode],
    ['Autokey cipher (Cifra de autochave)', cod_autokey, decod_autokey],
    ['Cifra niilista', cod_niilista, decod_niilista]
]


def programa() -> None:
    """Função que recebe qual das opções de criptografias o usuário quer executar"""
    print('\n' * 15)
    print('Menu principal\n')

    for opcao, valores in enumerate(opcoes_cripto):
        print(str(opcao + 1) + ' - ' + valores[0])
    print(str(len(opcoes_cripto) + 1) + ' - Sair do programa')
    print()

    try:
        opcao_escolhida: int = int(input('Digite umas da opções: '))
        efetuar_opcao(opcao_escolhida - 1)

    except ValueError:
        print('Opção inválida.')
    sleep(3)
    programa()


def codificar_ou_decodificar() -> int:
    """Função para saber se o usuário deseja codificar ou decodificar"""
    print('Codificar ou decodificar\n')
    print('1 - Codificar\n2 - Decodificar')

    try:
        escolha: int = int(input('Digite uma das opções: '))
        print('\n' * 15)
        if escolha == 1 or escolha == 2:
            return escolha
        else:
            print('Opção inválida')

    except ValueError:
        print('\n' * 15)
        print('Opção inválida')


def efetuar_opcao(escolha_cripto) -> None:
    """Função que verifica se o usuário escolheu uma opção válida, e se sim, ela é executada"""
    escolha_operacao = 0

    if 0 <= escolha_cripto < len(opcoes_cripto):
        while escolha_operacao != 1 and escolha_operacao != 2:
            escolha_operacao = codificar_ou_decodificar()
        print(opcoes_cripto[escolha_cripto][escolha_operacao]())

    elif escolha_cripto == len(opcoes_cripto):
        print('Programa finalizado.')
        exit()

    else:
        print('Opção inválida.')
