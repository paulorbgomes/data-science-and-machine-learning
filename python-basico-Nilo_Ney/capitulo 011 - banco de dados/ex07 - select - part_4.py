# select ... from ... where ...

import sqlite3

nome = input("Nome do contato a selecionar: ")

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# select ... from ... where ...
#cursor.execute("select * from agenda where nome = 'Nilo'")
#cursor.execute('''
#                select * from agenda where nome = "Nilo"
#               ''')
cursor.execute(f"select * from agenda where nome = '{nome}'")

resultado = cursor.fetchall()
#print(resultado)
for contato in resultado:
    print(f"Nome: {contato[0]}\nTelefone: {contato[1]}\n----------")

cursor.close()
conexao.close()
