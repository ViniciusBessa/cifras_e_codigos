from string import ascii_uppercase


def decodificar_cesar() -> str:
    """Função para decodificar de cifra de César"""
    alfabeto: list = [letra for letra in ascii_uppercase]

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


def decodificar_morse() -> str:
    """Função para decodificar de código morse"""
    alfabeto: list = [x for x in ascii_uppercase]
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


def decodificar_onetimepad() -> str:
    """Função para decodificar de one-time pad"""
    alfabeto: list = [x for x in ascii_uppercase]

    print('Decodificador de one-time pad\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ') if x.upper() in alfabeto]
    chave: list = [x.upper() for x in input('Digite a chave: ') if x.upper() in alfabeto]

    if len(chave) < len(mensagem):
        return 'A chave precisa ter no mínimo o mesmo número de letras que a mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) - alfabeto.index(chave[indice])) % 26]
    return f"Resultado: {''.join(mensagem)}"


def decodificar_tapcode() -> str:
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


def decodificar_vigenere() -> str:
    """Função para decodificar de cifra de Vigenère"""
    alfabeto: list = [letra for letra in ascii_uppercase]

    print('Decodificador de cifra de Vigenère\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ')]

    try:
        chave: list = [x.upper() for x in input('Digite a chave: ')]
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
