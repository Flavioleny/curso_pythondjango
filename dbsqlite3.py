import sqlite3
db=sqlite3.connect("senac.db")
cursor = db.cursor()

cursor.execute("""
create table if not exists alunos(id integer primary key autoincrement,
nome varchar(100) not null,
telefone varchar(14) not null,
email varchar(100) not null unique) """)
db.commit()

cursor.execute("""insert into alunos(nome,telefone,email) values("Flavio Santos",
"9472-1797","alguem4@hotmail.com"); """)
db.commit()

cursor.execute("select * from alunos;")
aluno1 = cursor.fetchall()
for a in aluno1:
    print(a)
    

