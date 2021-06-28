from string import ascii_uppercase

alfabeto: list = [x for x in ascii_uppercase]
numeros: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

tabela_alfa: list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                     '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
tabela_num: list = ['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']


def decodificar_morse() -> str:
    """Função para decodificar de código morse"""
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
