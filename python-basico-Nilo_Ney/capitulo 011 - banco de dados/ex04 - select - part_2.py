# select (multiple values) ...

import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# select ...
cursor.execute('''
                select * from agenda
               ''')
resultado = cursor.fetchall()
#print(resultado)
for registro in resultado:
    #print(registro)
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}\n----------")

cursor.close()
conexao.close()
