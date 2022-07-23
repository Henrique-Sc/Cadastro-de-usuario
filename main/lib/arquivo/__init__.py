from time import sleep


def arquivoExiste(nomeArquivo):
    try:
        with open(nomeArquivo, 'r'):
            pass

    except FileNotFoundError:
        with open(nomeArquivo, 'w+'):
            pass

    except:
        print('\033[37mErro ao criar o arquivo.')


def cadastrar(nomeArquivo, nome, idade):
    with open(nomeArquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
    sleep(1)
    print(f'\nCadastro realizado com sucesso!'.center(35))
    sleep(1)


def mostrarCadastro(nomeArquivo, tmn=35):
    with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
        listaCadastro = arquivo.readlines()

    if not listaCadastro:
        print('Nenhum cadastro encontrado.\n'.center(tmn))

    for cadastro in listaCadastro:
        cadastro = cadastro.replace('\n', '').split(';')
        print(f' {cadastro[0]:<{tmn - 11}} {cadastro[1]:<3}', 'ano' if int(cadastro[1]) <= 1 else 'anos')
        sleep(0.23)
    sleep(1)
