from lib.interface import *

while True:
    titulo('CADASTRO DE USUÁRIO', corSimb=4)
    esc = opcoes('Cadastrar', 'Lista dos cadastros', 'Sair do programa', corNum=1, corLinha=3)

    if esc == 1:
        titulo('Cadastrar', corSimb=3)
        print('aa')
        sleep(1)

    elif esc == 2:
        titulo('Lista dos cadastros', corSimb=3)
        print('aa')
        sleep(1)

    elif esc == 3:
        titulo('Saindo do programa...', corSimb=3)
        print(f'{cores[4]}{"-> Volte sempre! <-":^30}{cores[0]}')
        sleep(1)
        break
