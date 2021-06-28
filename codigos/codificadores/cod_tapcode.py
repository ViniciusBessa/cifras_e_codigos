from string import ascii_uppercase

# Tabela do tap code
tabela: list = [['A', 'B', 'C', 'D', 'E'],
                ['F', 'G', 'H', 'I', 'J'],
                ['L', 'M', 'N', 'O', 'P'],
                ['Q', 'R', 'S', 'T', 'U'],
                ['V', 'W', 'X', 'Y', 'Z']]


def codificar_tapcode() -> str:
    """Função para codificar em tap code"""
    print('Codificador de tap code')
    print('Escolha uma das opções\n')
    print('1 - Codificar para pontos')
    print('2 - Codificar para números')
    tipo_saida: str = input('Digite uma das opções: ')

    if tipo_saida == '1' or tipo_saida == '2':
        mensagem: list = [x.upper() for x in input('Digite a mensagem: ') if x.upper() in ascii_uppercase]
        for indice_msg, letra in enumerate(mensagem):
            for indice_lin, linha in enumerate(tabela):
                if letra in linha:
                    mensagem[indice_msg] = ','.join([str(indice_lin + 1), str(linha.index(letra) + 1)])
        if tipo_saida == '1':
            for indice, conjunto in enumerate(mensagem):
                lista = conjunto.split(',')
                mensagem[indice] = ' '.join(['.' * int(x) for x in lista])
        return f"Resultado: {'  '.join(mensagem)}"
    return 'Opção inválida.'
