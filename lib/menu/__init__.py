def menuprincipal():
    cabecalho('Menu Principal')
    print ('Menu: \n'
    '1 - Adicionar Veículo\n'
    '2 - Buscar um Veículo na frota\n'
    '3 - Listar todos os Veículos da frota\n'
    '4 - Remover um Veículo da frota\n'
    '5 - Atualizar Dados de um Veículo\n'
    '6 - Aluguel do Veículo\n'
    '7 - Devolver o Veículo\n'
    '8 - Carregar e salvar os dados\n'
    '0 - Sair Do Sistema\n')
    
    opc = int(input('Digite uma opção: '))
    print()
    return opc


def linha (tam = 42):
    return '-' * tam

def cabecalho (text):
    print(linha())
    print(text.center(42))
    print(linha())
    print()