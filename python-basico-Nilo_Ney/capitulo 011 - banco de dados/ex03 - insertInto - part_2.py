# insert into ...

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

# insert into (multiple values) ...
data = [("João", "98901-0109"),
        ("André", "98902-8900"),
        ("Maria", "97891-3321")]

cursor.executemany('''
                    insert into agenda (nome, telefone)
                    values(?, ?)''',
                   data)

conexao.commit()
cursor.close()
conexao.close()
