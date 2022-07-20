from time import sleep


def cadastrar(nomeArquivo, nome, idade):
    with open(nomeArquivo, 'at+') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
    sleep(1)
    print(f'\nCadastro realizado com sucesso!'.center(35))
    sleep(1)
