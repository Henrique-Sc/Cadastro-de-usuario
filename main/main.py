from time import sleep as s
import functions

while True:
    esc = functions.menu()
    functions.opcoes(esc)
    if esc == 3:
        break
