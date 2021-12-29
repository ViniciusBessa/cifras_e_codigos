from string import ascii_uppercase
from textwrap import wrap

alfabeto: list = list(ascii_uppercase)


def cod_cesar(mensagem: str, chave: int) -> str:
    """Função para codificar em cifra de César"""
    mensagem: list = [x.upper() for x in mensagem]
    novo_alfabeto: list = alfabeto[int(chave)::]
    novo_alfabeto.extend(alfabeto[0:int(chave):])
    carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if not x.isalpha()]
    mensagem: list = [novo_alfabeto[alfabeto.index(x)] for x in mensagem if x.isalpha()]
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return ''.join(mensagem)


def cod_morse(mensagem: str) -> str:
    """Função para codificar em código morse"""
    tabela_alfa: dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }
    tabela_num: dict = {
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }
    mensagem: list = [caractere.upper() for caractere in mensagem if caractere != ' ']
    for indice, seq in enumerate(mensagem):
        if seq in tabela_alfa:
            mensagem[indice] = tabela_alfa.get(seq)

        elif seq in tabela_num:
            mensagem[indice] = tabela_num.get(seq)
    return ' '.join(mensagem)


def cod_onetimepad(mensagem: str, chave: str) -> str:
    """Função para codificar em one-time pad"""
    mensagem: list = [x.upper() for x in mensagem if x.isalpha()]
    chave: list = [x.upper() for x in chave if x.isalpha()]

    if len(chave) < len(mensagem):
        return 'A chave precisa ter, no mínimo, o tamanho da mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) + alfabeto.index(chave[indice])) % 26]
    return ''.join(mensagem)


def cod_tapcode(mensagem: str, tipo_saida: int) -> str:
    # Tabela do tap code
    """Função para codificar em tap code"""
    tabela: list = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'J'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']]
    tipo_saida -= 1

    if tipo_saida == 0 or tipo_saida == 1:
        mensagem: list = [x.upper() for x in mensagem if x.isalpha()]
        for indice_msg, letra in enumerate(mensagem):
            for indice_lin, linha in enumerate(tabela):
                if letra in linha:
                    mensagem[indice_msg] = ','.join([str(indice_lin + 1), str(linha.index(letra) + 1)])
        if tipo_saida == 1:
            for indice, conjunto in enumerate(mensagem):
                lista = conjunto.split(',')
                mensagem[indice] = ' '.join(['.' * int(x) for x in lista])
        return '  '.join(mensagem)
    return 'Escolha uma das opções disponíveis.'


def cod_vigenere(mensagem: str, chave: str) -> str:
    """Função para codificar em cifra de Vigenère"""
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
        mensagem[indice] = novo_alfabeto[alfabeto.index(letra)]
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return ''.join(mensagem)


def cod_autokey(mensagem: str, chave: str):
    """Função para codificar em autokey cipher"""
    mensagem: list = [x.upper() for x in mensagem]
    chave: list = [x.upper() for x in chave]

    for letra in [x for x in mensagem if x.isalpha()]:
        if len(chave) < len([x for x in mensagem if x.isalpha()]):
            chave.append(letra)
        else:
            break
    carac_esp: list = [[indice, x] for indice, x in enumerate(mensagem) if not x.isalpha()]
    mensagem: list = [x for x in mensagem if x.isalpha()]
    for indice, letra in enumerate(mensagem):
        novo_alfabeto: list = alfabeto[alfabeto.index(chave[indice])::]
        novo_alfabeto.extend(alfabeto[0:alfabeto.index(chave[indice]):])
        mensagem[indice] = novo_alfabeto[alfabeto.index(letra)]
    for carac in carac_esp:
        mensagem.insert(carac[0], carac[1])
    return ''.join(mensagem)


def cod_niilista(mensagem: str, chave: str, palavra: str):
    """Função para codificar em cifra niilista"""
    alfabeto = [letra for letra in ascii_uppercase if letra != 'J']
    mensagem: list = [x.upper() for x in mensagem if x.isalpha() ]
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

    for indice_letra, letra in enumerate(mensagem):
        for indice_linha, linha in enumerate(tabela):
            if letra in linha:
                mensagem[indice_letra] = str(indice_linha + 1) + str(linha.index(letra) + 1)

    for indice_letra, letra in enumerate(chave):
        for indice_linha, linha in enumerate(tabela):
            if letra in linha:
                chave[indice_letra] = str(indice_linha + 1) + str(linha.index(letra) + 1)

    for n in range(len(mensagem)):
        mensagem[n] = str(int(mensagem[n]) + int(chave[n]))
    return ' '.join(mensagem)    
