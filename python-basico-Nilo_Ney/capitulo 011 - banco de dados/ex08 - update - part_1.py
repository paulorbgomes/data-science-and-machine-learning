# update ...

import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# update ...
cursor.execute('''
                update agenda
                set telefone = "12345-6789"
                where nome = "Nilo"
               ''')
conexao.commit()   # apos modificar o banco de dados devemos chamar o metodo commit()

print(f"Registros alterados: {cursor.rowcount}")

cursor.execute('''
                select * from agenda
               ''')
resultado = cursor.fetchall()
for contato in resultado:
    print(f"Nome: {contato[0]} | Telefone: {contato[1]}")

cursor.close()
conexao.close()
