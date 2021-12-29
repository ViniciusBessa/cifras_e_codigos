from string import ascii_uppercase
from textwrap import wrap

alfabeto: list = list(ascii_uppercase)


def decod_cesar(mensagem: str, chave: int) -> str:
    """Função para decodificar de cifra de César"""
    mensagem: list = [x.upper() for x in mensagem]
    novo_alfabeto: list = alfabeto[int(chave)::]
    novo_alfabeto.extend(alfabeto[0:int(chave):])
    carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if not x.isalpha()]
    mensagem: list = [alfabeto[novo_alfabeto.index(x)] for x in mensagem if x.isalpha()]
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return ''.join(mensagem)


def decod_morse(codigo: str) -> str:
    """Função para decodificar de código morse"""
    tabela_alfa: dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z' 
    }

    tabela_num: dict = {
        1: '.----', 2: '..---', 3: '...--', 4: '....-', 5: '.....', 
        6: '-....', 7: '--...', 8: '---..', 9: '----.', 0: '-----'
    }

    codigo: list = codigo.split()
    for indice, seq in enumerate(codigo):
        if len(seq) > 5:
            return 'O código não foi digitado corretamente'

        if seq in tabela_alfa:
            codigo[indice] = tabela_alfa.get(seq)
        
        elif seq in tabela_num:
            codigo[indice] = tabela_num.get(seq)
    return ''.join(codigo)


def decod_onetimepad(mensagem: str, chave: str) -> str:
    """Função para decodificar de one-time pad"""
    mensagem: list = [x.upper() for x in mensagem if x.isalpha()]
    chave: list = [x.upper() for x in chave if x.isalpha()]

    if len(chave) < len(mensagem):
        return 'A chave precisa ter no mínimo o mesmo número de letras que a mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) - alfabeto.index(chave[indice])) % 26]
    return ''.join(mensagem)


def decod_tapcode(codigo: str, tipo_entrada: int) -> str:
    """Função para decodificar de tap code"""
    tabela: list = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'J'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']]
    tipo_entrada = tipo_entrada - 1

    if tipo_entrada == 0:
        codigo: list = codigo.split()
        codigo = [tabela[int(x) - 1][int(y) - 1] for x, y in [z.split(',') for z in codigo]]
        return ''.join(codigo)

    elif tipo_entrada == 1:
        codigo: list = codigo.split("  ")
        codigo = [tabela[len(x) - 1][len(y) - 1] for x, y in [z.split(" ") for z in codigo]]
        return ''.join(codigo)


def decod_vigenere(mensagem: str, chave: str) -> str:
    """Função para decodificar de cifra de Vigenère"""
    mensagem: list = [x.upper() for x in mensagem]
    chave: list = [x.upper() for x in chave]

    for letra in chave:
        if len(chave) < len([x for x in mensagem if x.isalpha()]):
            chave.append(letra)
        else:
            break
    carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if not x.isalpha()]
    mensagem: list = [x for x in mensagem if x.isalpha()]
    for indice, letra in enumerate(mensagem):
        novo_alfabeto: list = alfabeto[alfabeto.index(chave[indice])::]
        novo_alfabeto.extend(alfabeto[0:alfabeto.index(chave[indice]):])
        mensagem[indice] = alfabeto[novo_alfabeto.index(letra)]
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return ''.join(mensagem)


def decod_autokey(mensagem: str, chave: str):
    """Função para decodificar de autokey cipher"""
    mensagem: list = [x.upper() for x in mensagem]
    chave: list = [x.upper() for x in chave]
    carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if not x.isalpha()]
    mensagem: list = [x for x in mensagem if x.isalpha()]
    for indice, letra in enumerate(mensagem):
        novo_alfabeto: list = alfabeto[alfabeto.index(chave[indice])::]
        novo_alfabeto.extend(alfabeto[0:alfabeto.index(chave[indice]):])
        mensagem[indice] = alfabeto[novo_alfabeto.index(letra)]
        chave.append(mensagem[indice])
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return ''.join(mensagem)


def decod_niilista(mensagem: str, chave: str, palavra: str):
    """Função para decodificar de cifra niilista"""
    alfabeto = [letra for letra in ascii_uppercase if letra != 'J']
    mensagem: list = mensagem.split()
    tabela: list = []
    palavra: list = [x.upper() for x in palavra if x.isalpha() and x.upper() != 'J']
    for letra in ''.join(palavra) + ''.join(alfabeto):
        if letra not in tabela:
            tabela.append(letra)
    chave: list = [x.upper() for x in chave if x.isalpha()]

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
