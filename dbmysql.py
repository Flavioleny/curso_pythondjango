import MySQLdb

db= MySQLdb.connect(host='localhost', user='root', passwd='123',db='senac')
cursor = db.cursor()

cursor.execute("select * from alunos;")
aluno1 = cursor.fetchall()
for a in aluno1:
    print(a)
