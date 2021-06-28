from string import ascii_uppercase

alfabeto: list = [letra for letra in ascii_uppercase]


def decodificar_cesar() -> str:
    """Função para decodificar de cifra de César"""
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
        return f"Resulado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')
