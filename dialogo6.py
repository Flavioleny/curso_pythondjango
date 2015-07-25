try:
    dialogo = open('dialogo.txt')
    dialogo.seek(0)
    for linha in dialogo:
        try:
            ator,fala = linha.split(':',1)
            print(ator,end='')
            print(' diz: ', end='')
            print(fala,end='')
        except ValueError:
            pass
    dialogo.close()
except FileNotFoundError: #Ou IOError
    print('O arquivo nao existe.')
