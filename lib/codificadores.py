from string import ascii_uppercase


def codificar_cesar() -> str:
    """Função para codificar em cifra de César"""
    alfabeto: list = [letra for letra in ascii_uppercase]

    print('Codificador de cifra de César\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será codificada: ')]

    try:
        chave: int = int(input('Digite a chave que será utilizada na codificação (0-25): '))
        novo_alfabeto: list = alfabeto[int(chave)::]
        novo_alfabeto.extend(alfabeto[0:int(chave):])
        carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if x not in alfabeto]
        mensagem: list = [novo_alfabeto[alfabeto.index(x)] for x in mensagem if x in alfabeto]
        for carac in carac_esp:
            mensagem.insert(carac[0], carac[1])
        return f"Resultado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')


def codificar_morse() -> str:
    """Função para codificar em código morse"""
    alfabeto: list = [x for x in ascii_uppercase]
    numeros: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    tabela_alfa: list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                         '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    tabela_num: list = ['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

    print('Codificador de código morse\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será convertida em código morse: ') if x != ' ']

    for indice, carac in enumerate(mensagem):
        if carac in alfabeto:
            mensagem[indice] = tabela_alfa[alfabeto.index(carac)]
        elif carac in numeros:
            mensagem[indice] = tabela_num[numeros.index(carac)]
    return f"Resultado: {' '.join(mensagem)}"


def codificar_onetimepad() -> str:
    """Função para codificar em one-time pad"""
    alfabeto: list = [x for x in ascii_uppercase]

    print('Codificador de one-time pad\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será codificada: ') if x.upper() in alfabeto]
    chave: list = [x.upper() for x in input('Digite a chave: ') if x.upper() in alfabeto]

    if len(chave) < len(mensagem):
        return 'A chave precisa ter no mínimo o mesmo número de letras que a mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) + alfabeto.index(chave[indice])) % 26]
    return f"Resultado: {''.join(mensagem)}"


def codificar_tapcode() -> str:
    """Função para codificar em tap code"""
    # Tabela do tap code
    tabela: list = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'J'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']]

    print('Codificador de tap code')
    print('Escolha uma das opções\n')
    print('1 - Codificar para pontos')
    print('2 - Codificar para números')
    tipo_saida: str = input('Digite uma das opções: ')

    if tipo_saida == '1' or tipo_saida == '2':
        mensagem: list = [x.upper() for x in input('Digite a mensagem: ') if x.upper() in ascii_uppercase]
        for indice_msg, letra in enumerate(mensagem):
            for indice_lin, linha in enumerate(tabela):
                if letra in linha:
                    mensagem[indice_msg] = ','.join([str(indice_lin + 1), str(linha.index(letra) + 1)])
        if tipo_saida == '1':
            for indice, conjunto in enumerate(mensagem):
                lista = conjunto.split(',')
                mensagem[indice] = ' '.join(['.' * int(x) for x in lista])
        return f"Resultado: {'  '.join(mensagem)}"
    return 'Opção inválida.'


def codificar_vigenere() -> str:
    """Função para codificar em cifra de Vigenère"""
    alfabeto: list = [letra for letra in ascii_uppercase]

    print('Codificador de cifra de Vigenère\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será codificada: ')]

    try:
        chave: list = [x.upper() for x in input('Digite a chave que será utilizada na codificação: ')]
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
            mensagem[indice] = novo_alfabeto[alfabeto.index(letra)]
        for carac in carac_esp:
            mensagem.insert(carac[0], carac[1])
        return f"Resultado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')
