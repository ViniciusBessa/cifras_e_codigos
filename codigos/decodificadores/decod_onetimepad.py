from string import ascii_uppercase

alfabeto: list = [x for x in ascii_uppercase]


def decodificar_onetimepad() -> str:
    """Função para decodificar de one-time pad"""
    print('Decodificador de one-time pad\n')
    mensagem: list = [x.upper() for x in input('Digite a mensagem que será decodificada: ') if x.upper() in alfabeto]
    chave: list = [x.upper() for x in input('Digite a chave: ') if x.upper() in alfabeto]
    if len(chave) < len(mensagem):
        return 'A chave precisa ter no mínimo o mesmo número de letras que a mensagem.'
    for indice, letra in enumerate(mensagem):
        mensagem[indice] = alfabeto[(alfabeto.index(letra) - alfabeto.index(chave[indice])) % 26]
    return f"Resultado: {''.join(mensagem)}"
