from string import ascii_uppercase

alfabeto: list = [letra for letra in ascii_uppercase]


def codificar_cesar() -> str:
    """Função para codificar em cifra de César"""
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
        return f"Resulado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')
