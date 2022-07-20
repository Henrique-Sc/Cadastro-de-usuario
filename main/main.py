from lib.interface import *
from lib.arquivo import *
from lib.dado import *

arquivoExiste('cadastros.txt')
while True:
    titulo('CADASTRO DE USUÁRIO', corSimb=4)
    esc = opcoes('Cadastrar', 'Lista dos cadastros', 'Sair do programa', corNum=1, corLinha=3)

    # Cadastrar
    if esc == 1:
        titulo('Cadastrar', corSimb=3)

        nome = leiaNome('Digite o seu nome: ')
        idade = leiaIdade('Digite a sua idade: ')
        cadastrar(nome, idade)

    # Listar os cadastros
    elif esc == 2:
        titulo('Lista dos cadastros', corSimb=3)

    # Sair do programa
    elif esc == 3:
        titulo('Saindo do programa...', corSimb=3)
        print(f'{cores[4]}{"-> Volte sempre! <-":^30}{cores[0]}')
        sleep(1)
        break
