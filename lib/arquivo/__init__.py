def adicionarveiculo(veiculos, id, marca, modelo, ano, placa, cor, valordiaria, disponivel ):
    veiculo = { 'Id': id,
                'Marca': marca,
                'Modelo': modelo,
                'Ano': ano ,
                'Placa': placa ,
                'Cor': cor ,
                'ValorDiaria': valordiaria ,
                'Disponivel': disponivel }
    veiculos.append(veiculo)


def buscarveiculo (veiculos, busca):
    for veiculo in veiculos:
        if veiculo ['Id'] == busca:
            print(f' - Id = {veiculo['Id']}')
            print(f' - Marca = {veiculo['Marca']} ')
            print(f' - Modelo = {veiculo['Modelo']} ')
            print(f' - Ano = {veiculo['Ano']} ')
            print(f' - Placa = {veiculo['Placa']} ')
            print(f' - Cor = {veiculo['Cor']} ')
            print(f' - Valor Diária = R$ {veiculo['ValorDiaria']} ')
            print(f' - Disponível = {veiculo['Disponivel']}\n ')
            return True
    print('Veículo não Encontrado. ')
    return False

def listarveiculos(veiculos):
    for veiculo in veiculos:
        print(f' - Id = {veiculo['Id']}')
        print(f' - Marca = {veiculo['Marca']} ')
        print(f' - Modelo = {veiculo['Modelo']} ')
        print(f' - Ano = {veiculo['Ano']} ')
        print(f' - Placa = {veiculo['Placa']} ')
        print(f' - Cor = {veiculo['Cor']} ')
        print(f' - Valor Diária = R$ {veiculo['ValorDiaria']} ')
        print(f' - Disponível = {veiculo['Disponivel']}\n ')
    print()


def atualizarveiculo(veiculos, busca, marca, modelo, ano, placa, cor, valordiaria):
    for veiculo in veiculos:
        if veiculo['Id'] == busca:
            veiculo['Marca'] = marca
            veiculo['Modelo'] = modelo
            veiculo['Ano'] = ano
            veiculo['Placa'] = placa
            veiculo['Cor'] = cor
            veiculo['ValorDiaria'] = valordiaria
            return True
    print()
    return False


def removerveiculo(veiculos, busca):
    for veiculo in veiculos:
        if veiculo ['Id'] == busca:
            veiculos.remove(veiculo)
            break


def lerdados(veiculos):
    arquivo = open('dados.txt', 'r')
    cont = 5000
    linhas = arquivo.readlines()
    teste = False
    for linha in linhas:
        if teste == False:
            cont = int(linha)
            teste = True
            continue
        termo =  linha.split(';')
        veiculo = {}
        veiculo['Id'] = int(termo[0])
        veiculo['Marca'] = termo[1]
        veiculo['Modelo'] = termo[2]
        veiculo['Ano'] = int(termo[3])
        veiculo['Placa'] = termo[4]
        veiculo['Cor'] = termo [5]
        veiculo['ValorDiaria'] = float(termo[6])
        veiculo['Disponivel'] = termo[7] = 'True'
        veiculos.append(veiculo)
    arquivo.close()
    return cont


def salvardados(veiculos, cont):
    arquivo = open('dados.txt', 'w')
    arquivo.write(f'{cont}\n')
    for veiculo in veiculos:
        arquivo.write(f'{veiculo['Id']};')
        arquivo.write(f'{veiculo['Marca']};')
        arquivo.write(f'{veiculo['Modelo']};')
        arquivo.write(f'{veiculo['Ano']};')
        arquivo.write(f'{veiculo['Placa']};')
        arquivo.write(f'{veiculo['Cor']};')
        arquivo.write(f'{veiculo['ValorDiaria']};')
        arquivo.write(f'{veiculo['Disponivel']};\n')
    arquivo.close()