# select (multiple values) ...

import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# select ...
cursor.execute('''
                select * from agenda
              ''')
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    else:
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}\n----------")

cursor.close()
conexao.close()
