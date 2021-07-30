from string import ascii_uppercase
from textwrap import wrap


def decod_cesar() -> str:
    """Função para decodificar de cifra de César"""
    alfabeto: list = list(ascii_uppercase)

    print('Decodificador de cifra de César\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ')]

    try:
        chave: int = int(input('Digite a chave que será utilizada na decodificação (0-25): '))
        novo_alfabeto: list = alfabeto[chave::]
        novo_alfabeto.extend(alfabeto[0:chave:])
        carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if x not in alfabeto]
        mensagem: list = [alfabeto[novo_alfabeto.index(x)] for x in mensagem if x in alfabeto]
        for carac in carac_esp:
            mensagem.insert(carac[0], carac[1])
        return f"Resultado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')


def decod_morse() -> str:
    """Função para decodificar de código morse"""
    alfabeto: list = list(ascii_uppercase)

    numeros: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    tabela_alfa: list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                         '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    tabela_num: list = ['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

    print('Decodificador de código morse\n')
    codigo: list = input('Digite o código morse, com espaço entre cada sequência: ').split()

    for indice, seq in enumerate(codigo):
        if len(seq) > 5:
            return 'O código não foi digitado corretamente'
        if seq in tabela_alfa:
            codigo[indice] = alfabeto[tabela_alfa.index(seq)]
        elif seq in tabela_num:
            codigo[indice] = numeros[tabela_num.index(seq)]
    return f"Resultado: {''.join(codigo)}"


def decod_onetimepad() -> str:
    """Função para decodificar de one-time pad"""
    alfabeto: list = list(ascii_uppercase)

    print('Decodificador de one-time pad\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ') if x.upper() in alfabeto]
    chave: list = [x.upper() for x in input('Digite a chave: ') if x.upper() in alfabeto]

    if len(chave) < len(mensagem):
        return 'A chave precisa ter no mínimo o mesmo número de letras que a mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) - alfabeto.index(chave[indice])) % 26]
    return f"Resultado: {''.join(mensagem)}"


def decod_tapcode() -> str:
    """Função para decodificar de tap code"""
    # Tabela do tap code
    tabela: list = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'J'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']]

    print('Decodificador de tap code')
    print('Escolha uma das opções\n')
    print('1 - Decodificar de pontos')
    print('2 - Decodificar de números')
    tipo_entrada: str = input('Digite uma das opções: ')

    if tipo_entrada == '1':
        print('Escreva o código com espaço entre os números e dois espaços entre cada série')
        print('Exemplo: . ...  ... ..\n')
        codigo: list = input('Digite o código: ').split("  ")
        try:
            codigo = [tabela[len(x) - 1][len(y) - 1] for x, y in [z.split(" ") for z in codigo]]
            return f"Resultado: {''.join(codigo)}"
        except ValueError:
            return 'O código não foi digitado corretamente.'

    elif tipo_entrada == '2':
        print('Escreva o código com vírgula entre os números e espaço entre cada série')
        print('Exemplo: 1,3 2,1 4,5\n')
        codigo: list = input('Digite o código: ').split()
        try:
            codigo = [tabela[int(x) - 1][int(y) - 1] for x, y in [z.split(',') for z in codigo]]
            return f"Resultado: {''.join(codigo)}"
        except ValueError:
            return 'O código não foi digitado corretamente.'
    return 'Opção inválida.'


def decod_vigenere() -> str:
    """Função para decodificar de cifra de Vigenère"""
    alfabeto: list = list(ascii_uppercase)

    print('Decodificador de cifra de Vigenère\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ')]
    chave: list = [x.upper() for x in input('Digite a chave: ')]

    try:
        for letra in chave:
            if len(chave) < len([x for x in mensagem if x in alfabeto]):
                chave.append(letra)
            else:
                break
        carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if x not in alfabeto]
        mensagem: list = [x for x in mensagem if x in alfabeto]
        for indice, letra in enumerate(mensagem):
            novo_alfabeto: list = alfabeto[alfabeto.index(chave[indice])::]
            novo_alfabeto.extend(alfabeto[0:alfabeto.index(chave[indice]):])
            mensagem[indice] = alfabeto[novo_alfabeto.index(letra)]
        for carac in carac_esp:
            mensagem.insert(carac[0], carac[1])
        return f"Resultado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')


def decod_autokey():
    """Função para decodificar de cifra de autochave"""
    alfabeto: list = list(ascii_uppercase)

    print('Decodificador de cifra de autochave\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ')]
    chave: list = [x.upper() for x in input('Digite a chave: ')]

    try:
        carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if x not in alfabeto]
        mensagem: list = [x for x in mensagem if x in alfabeto]
        for indice, letra in enumerate(mensagem):
            novo_alfabeto: list = alfabeto[alfabeto.index(chave[indice])::]
            novo_alfabeto.extend(alfabeto[0:alfabeto.index(chave[indice]):])
            mensagem[indice] = alfabeto[novo_alfabeto.index(letra)]
            chave.append(mensagem[indice])
        for carac in carac_esp:
            mensagem.insert(carac[0], carac[1])
        return f"Resultado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')


def decod_niilista():
    """Função para decodificar de cifra niilista"""
    alfabeto: list = [letra for letra in ascii_uppercase if letra != 'J']

    print('Decodificador de cifra niilista\n')
    mensagem: list = input('Digite a mensagem que será decodificada: ').split()
    tabela: list = []

    try:
        palavra: str = input('Digite a palavra-chave usada no quadrado de Políbio: ')
        palavra: list = [x.upper() for x in palavra if x.upper() in alfabeto and x.upper() != 'J']
        for letra in ''.join(palavra) + ''.join(alfabeto):
            if letra not in tabela:
                tabela.append(letra)
        chave: list = [x.upper() for x in input('Digite a chave utilizada na codificação: ') if x.upper() in alfabeto]
        for letra in chave:
            if len(chave) < len(mensagem):
                chave.append(letra)
            else:
                break
        tabela = wrap(''.join(tabela), 5)

        for indice_letra, letra in enumerate(chave):
            for indice_linha, linha in enumerate(tabela):
                if letra in linha:
                    chave[indice_letra] = str(indice_linha + 1) + str(linha.index(letra) + 1)
        for n in range(len(mensagem)):
            mensagem[n] = str(int(mensagem[n]) - int(chave[n]))
        mensagem = [tabela[int(x[0]) - 1][int(x[1]) - 1] for x in mensagem]
        return ''.join(mensagem)
    except ValueError:
        return 'Chave inserida é inválida.'
