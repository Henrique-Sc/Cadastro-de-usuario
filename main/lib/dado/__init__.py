from time import sleep


def msgErro(msg):
    print(f'\n\033[31m{msg}\033[m\n')
    sleep(1)


def leiaNome(msg):
    print('\033[37mMáximo de 22 caracteres.\033[m')
    while True:
        try:
            nome = str(input(msg)).strip().title()

        except (KeyboardInterrupt, InterruptedError):
            msgErro('ERRO: Programa interrompido pelo usuário.')

        else:
            if len(nome) > 22:
                msgErro('ERRO: Nome maior que 22 caracteres.')
            elif len(nome) < 3:
                msgErro(f'ERRO: \'{nome}\' não é um nome válido.')

            else:
                return nome


def leiaIdade(msg):
    while True:
        try:
            idade = int(input(msg).strip()[:3])

        except (InterruptedError, KeyboardInterrupt):
            msgErro('ERRO: Programa interrompido pelo usuário.')

        except (ValueError, TypeError):
            msgErro('ERRO: Digite um número inteiro.')

        else:
            if idade < 0:
                msgErro(f'ERRO: \'{idade}\' não é uma idade válida.')
            else:
                return idade
