from string import ascii_uppercase

alfabeto: list = [x for x in ascii_uppercase]
numeros: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

tabela_alfa: list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                     '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
tabela_num: list = ['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']


def codificar_morse() -> str:
    """Função para codificar em código morse"""
    print('Codificador de código morse\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será convertida em código morse: ') if x != ' ']

    for indice, carac in enumerate(mensagem):
        if carac in alfabeto:
            mensagem[indice] = tabela_alfa[alfabeto.index(carac)]
        elif carac in numeros:
            mensagem[indice] = tabela_num[numeros.index(carac)]
    return f"Resultado: {' '.join(mensagem)}"
