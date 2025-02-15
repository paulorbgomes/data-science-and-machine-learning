# select ...

import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# select ...
cursor.execute('''
                select * from agenda
               ''')
resultado = cursor.fetchone()
#print(resultado)
print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")

cursor.close()
conexao.close()
