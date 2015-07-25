dialogo = open('dialogo.txt')
dialogo.seek(0)
for linha in dialogo:
    try:
        ator,fala = linha.split(':',1)
        print(ator,end='')
        print(' diz: ', end='')
        print(fala,end='')
    except:
        pass
dialogo.close()
