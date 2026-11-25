from time import sleep
from lib.menu import menuprincipal, cabecalho
from lib.arquivo import adicionarveiculo, listarveiculos, salvardados, lerdados, buscarveiculo

veiculos = lerdados ()
while True:
    opc= menuprincipal()

    if opc == 1:
        cabecalho('Cadastrar Novo Veículo')
        id = int(input('1 - Id: '))
        marca = str(input('2 - Marca: ')).strip().capitalize()
        modelo = str(input('3 - Modelo: ')).strip().capitalize()
        ano = int(input('4 - Ano: '))
        placa = str(input('5 - Placa: ')).strip().upper()
        cor = str(input('6 - Cor: ')).strip().capitalize()
        valordiaria = float(input('7 - Valor da Diária: R$ '))
        disponivel = True
        adicionarveiculo(veiculos, id, marca, modelo, ano, placa, cor, valordiaria, disponivel)
    elif opc == 2:
        busca = int(input('Digite o código: '))
        buscarveiculo(veiculos, busca)
    elif opc == 3:
        cabecalho('Veículos Disponíveis')
        listarveiculos(veiculos)
        sleep(5)

    elif opc == 4:
        print('remover')
    elif opc == 5:
        print('atualizar')
    elif opc == 6:
        print('Realizar um aluguel')
    elif opc == 7:
        print('Devolver')
    elif opc == 8:
        print('Carregar e Salvar')
    elif opc == 0:
        print('Saindo Do Sistema...')
        salvardados(veiculos)
        sleep(1)
        break
    else:
        print('Erro! Código Inválido')
        sleep(1)

