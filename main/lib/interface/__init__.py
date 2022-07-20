from time import sleep

cores = [
    '\033[m',    # 0 - Sem cor
    '\033[31m',  # 1 - Vermelho
    '\033[32m',  # 2 - Verde
    '\033[33m',  # 3 - Amarelo
    '\033[34m',  # 4 - Azul
    '\033[35m',  # 5 - Lilás
    '\033[36m',  # 6 - Ciano
    '\033[37m',  # 7 - Cinza
]


def linha(tmh=30, simb='=', corSimb=0):
    print(f'{cores[corSimb]}{simb}{cores[0]}' * tmh)


def titulo(msg, simb='=', corMsg=0, corSimb=0, tmn=30):
    linha(tmn, simb, corSimb)
    print(cores[corMsg] + msg.center(tmn) + cores[0])
    linha(tmn, simb, corSimb)

    sleep(0.8)


def msgErro(msg):
    print(f'\n{cores[1]}{msg}{cores[0]}\n')
    sleep(1)


def opcoes(*opcoes, corNum=0, corLinha):
    while True:
        # Listar as opções
        linha(corSimb=corLinha)
        for c, opcao in enumerate(opcoes, start=1):
            print(f' {cores[corNum]}{c}{cores[0]} - {opcao}')
            sleep(0.25)
        sleep(0.25)
        linha(corSimb=corLinha)

        try:
            opcao = int(input(f'O que deseja fazer? ').strip())

        except ValueError:
            msgErro('ERRO: Digite um número inteiro.')

        except KeyboardInterrupt:
            msgErro('ERRO: Você preferiu não digitar esse número.')
        else:
            if opcao < 1 or opcao > len(opcoes):
                msgErro('ERRO: Digite uma opção válida.')

            else:
                break

    return opcao
