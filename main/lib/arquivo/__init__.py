from time import sleep


def cadastrar(nomeArquivo, nome, idade):
    with open(nomeArquivo, 'at+') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
    sleep(1)
    print(f'\nCadastro realizado com sucesso!'.center(35))
    sleep(1)


def mostrarCadastro(nomeArquivo, tmn=35):
    with open(nomeArquivo, 'rt+') as arquivo:
        for cadastro in arquivo:
            cadastro = cadastro.replace('\n', '').split(';')
            print(f' {cadastro[0]:<{tmn-11}} {cadastro[1]:<3}', 'ano' if int(cadastro[1]) <= 1 else 'anos')
            sleep(0.23)
    sleep(0.90)