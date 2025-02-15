# primary key ...

dados = [
         ["São Paulo", 43663672],
         ["Minas Gerais", 20593366]
        ]

import sqlite3

conexao = sqlite3.connect("estados.db")
cursor = conexao.cursor()
'''
# create table ...
cursor.execute("""
                create table estados (
                    id integer primary key autoincrement,
                    nome text,
                    populacao integer
                )
               """)
'''

'''
# insert into ...
cursor.executemany("""
                    insert into estados (nome, populacao)
                    values(?, ?)""", dados)
conexao.commit()
'''

# select ...
cursor.execute("""
                select * from estados
               """)
resultado = cursor.fetchall()
for i in resultado:
    print(f"Estado: {i[1]}; População: {i[2]}")

# update ...
cursor.execute("""
                update estados set populacao = '0' 
               """)

# select ...
cursor.execute("""
                select * from estados
               """)
resultado = cursor.fetchall()
for i in resultado:
    print(f"Estado: {i[1]}; População: {i[2]}")

cursor.close()
conexao.close()
