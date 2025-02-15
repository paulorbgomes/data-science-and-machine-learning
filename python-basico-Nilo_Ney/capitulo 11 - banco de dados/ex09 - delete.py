# delete ...

import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute('''
                select * from agenda
               ''')
contatos = cursor.fetchall()
for registro in contatos:
    print(f"Nome: {registro[0]}; Telefone: {registro[1]}")

# delete ...
cursor.execute('''
                delete from agenda where nome = "Maria"
              ''')
conexao.commit()

cursor.execute('''
                select * from agenda
               ''')
contatos = cursor.fetchall()
for registro in contatos:
    print(f"Nome: {registro[0]}; Telefone: {registro[1]}")

cursor.close()
conexao.close()
