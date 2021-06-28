from string import ascii_uppercase

alfabeto: list = [letra for letra in ascii_uppercase]


def decodificar_vigenere() -> str:
    """Função para codificar em cifra de Vigenère"""
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
            novo_alfabeto = alfabeto[alfabeto.index(chave[indice])::]
            novo_alfabeto.extend(alfabeto[0:alfabeto.index(chave[indice]):])
            mensagem[indice] = alfabeto[novo_alfabeto.index(letra)]
        for carac in carac_esp:
            mensagem.insert(carac[0], carac[1])
        return f"Resulado: {''.join(mensagem)}"
    except ValueError:
        print('Chave inserida é inválida.')
