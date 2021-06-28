# Tabela do tap code
tabela: list = [['A', 'B', 'C', 'D', 'E'],
                ['F', 'G', 'H', 'I', 'J'],
                ['L', 'M', 'N', 'O', 'P'],
                ['Q', 'R', 'S', 'T', 'U'],
                ['V', 'W', 'X', 'Y', 'Z']]


def decodificar_tapcode() -> str:
    """Função para decodificar de tap code"""
    print('Decodificador de tap code')
    print('Escolha uma das opções\n')
    print('1 - Decodificar de pontos')
    print('2 - Decodificar de números')
    tipo_entrada: str = input('Digite uma das opções: ')

    if tipo_entrada == '1':
        print('Escreva o código com espaço entre os números e dois espaços entre cada série')
        print('Exemplo: . ...  ... ..\n')
        codigo: list = input('Digite o código: ').split("  ")
        try:
            codigo = [tabela[len(x) - 1][len(y) - 1] for x, y in [z.split(" ") for z in codigo]]
            return f"Resultado: {''.join(codigo)}"
        except ValueError:
            return 'O código não foi digitado corretamente.'

    elif tipo_entrada == '2':
        print('Escreva o código com vírgula entre os números e espaço entre cada série')
        print('Exemplo: 1,3 2,1 4,5\n')
        try:
            codigo: list = input('Digite o código: ').split()
            codigo = [tabela[int(x) - 1][int(y) - 1] for x, y in [z.split(',') for z in codigo]]
            return f"Resultado: {''.join(codigo)}"
        except ValueError:
            return 'O código não foi digitado corretamente.'
    return 'Opção inválida.'
