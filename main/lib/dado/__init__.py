from time import sleep


def msgErro(msg):
    print(f'\n\033[31m{msg}\033[m\n')
    sleep(1)


def leiaNome(msg):
    print('\033[37mMáximo de 20 caracteres.\033[m')
    while True:
        try:
            nome = str(input(msg)).strip().title().strip()

        except KeyboardInterrupt:
            pass

        else:
            if len(nome) > 20:
                msgErro('ERRO: Nome maior que 20 caracteres.')
            else:
                break

#
# def leiaIdade(msg):
#     while True:
#         try:
#