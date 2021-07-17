from string import ascii_uppercase


def decod_cesar(mensagem: str, chave: int) -> str:
    """Função para decodificar de cifra de César"""
    alfabeto: list = [letra for letra in ascii_uppercase]
    mensagem: list = [x.upper() for x in mensagem]

    novo_alfabeto: list = alfabeto[int(chave)::]
    novo_alfabeto.extend(alfabeto[0:int(chave):])
    carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if x not in alfabeto]
    mensagem: list = [alfabeto[novo_alfabeto.index(x)] for x in mensagem if x in alfabeto]
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return f"{''.join(mensagem)}"


def decod_morse(codigo: str) -> str:
    """Função para decodificar de código morse"""
    alfabeto: list = [x for x in ascii_uppercase]
    numeros: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    tabela_alfa: list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                         '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    tabela_num: list = ['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']
    codigo: list = codigo.split()

    for indice, seq in enumerate(codigo):
        if len(seq) > 5:
            return 'O código não foi digitado corretamente'
        if seq in tabela_alfa:
            codigo[indice] = alfabeto[tabela_alfa.index(seq)]
        elif seq in tabela_num:
            codigo[indice] = numeros[tabela_num.index(seq)]
    return f"{''.join(codigo)}"


def decod_onetimepad(mensagem: str, chave: str) -> str:
    """Função para decodificar de one-time pad"""
    alfabeto: list = [x for x in ascii_uppercase]
    mensagem: list = [x.upper() for x in mensagem if x.upper() in alfabeto]
    chave: list = [x.upper() for x in chave if x.upper() in alfabeto]

    if len(chave) < len(mensagem):
        return 'A chave precisa ter no mínimo o mesmo número de letras que a mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) - alfabeto.index(chave[indice])) % 26]
    return f"{''.join(mensagem)}"


def decod_tapcode(codigo: str, tipo_entrada: int) -> str:
    """Função para decodificar de tap code"""
    tabela: list = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'J'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']]

    if tipo_entrada == 0:
        codigo: list = codigo.split()
        codigo = [tabela[int(x) - 1][int(y) - 1] for x, y in [z.split(',') for z in codigo]]
        return f"{''.join(codigo)}"

    elif tipo_entrada == 1:
        codigo: list = codigo.split("  ")
        codigo = [tabela[len(x) - 1][len(y) - 1] for x, y in [z.split(" ") for z in codigo]]
        return f"{''.join(codigo)}"


def decod_vigenere(mensagem: str, chave: str) -> str:
    """Função para decodificar de cifra de Vigenère"""
    alfabeto: list = [letra for letra in ascii_uppercase]
    mensagem: list = [x.upper() for x in mensagem]
    chave: list = [x.upper() for x in chave]

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
    return f"{''.join(mensagem)}"
