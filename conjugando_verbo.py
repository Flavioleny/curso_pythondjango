import sqlite3,os
db=sqlite3.connect("senac.db")
cursor = db.cursor()

def selectVerbo():
    cursor.execute("select usuario,verbo,count(*) qtdvezes from verbo group by usuario,verbo;")
    verbo = cursor.fetchall()
    for a in verbo:
        print(a)    
    print("")    

def insertVerbo(usua,verb):
    cursor.execute("""insert into verbo(usuario,verbo) values('""" + str(usua) + """','"""+ str(verb)+"""'); """)
    db.commit()
    
#Primeiro criamos listas com as terminações de verbos regulares
pessoas = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles']
conjuga_ar = ['o', 'as', 'a', 'amos', 'ais', 'am']
conjuga_er = ['o', 'es', 'e', 'emos', 'eis', 'em']
conjuga_ir = ['o', 'es', 'e', 'imos', 'is', 'em']

verbo_regular = 0
conjugar_verbo = True
while conjugar_verbo != False:
    while True:  
        #a seguir, pedimos que o usuário informe o verbo
        usuario = input('Digite o Usuario que esta interagindo com o Aplicativo: ')
        verbo   = input('Digite o infinitivo de um verbo regular: ')

        #separa a terminação do verbo
        termina_em = verbo[-2:]

        #agora, de acordo com a terminação do verbo, conjuga apropriadamente
        if termina_em == 'ar':
            for i in range(6): #repete seis vezes, percorrendo a lista
                print(pessoas[i]+ ' ' + verbo[:-2]+conjuga_ar[i])
            break
        elif termina_em == 'er':
            for i in range(6): #repete seis vezes, percorrendo a lista
                print(pessoas[i]+ ' ' + verbo[:-2]+conjuga_er[i])
            break                
        elif termina_em == 'ir':
            for i in range(6): #repete seis vezes, percorrendo a lista
                print(pessoas[i]+ ' ' + verbo[:-2]+conjuga_ir[i])
            break                
        else:
            print("Tem certeza que " +verbo.upper()+ " é um verbo regular?")            
            verbo_regular = 1
            break

    if verbo_regular == 0:
        insertVerbo(usuario,verbo)
        print("Fim da conjugaçao do Verbo!!!" + str(verbo))
        
    selectVerbo()

    conjugar_verbo = int(input("Deseja conjugar outro Verbo Regular? 1 - Sim ou 0 - Não: "))
    os.system("Clear")
