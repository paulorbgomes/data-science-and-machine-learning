# BD SQLite vem pre-instalado no interpretador Python ...

# create data base | create table | insert into ...

import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# create table ...
cursor.execute('''
                create table agenda (
                    nome text,
                    telefone text
                )
              ''')

# insert into ...
cursor.execute('''
                insert into agenda (nome, telefone)
                values(?, ?)''',
               ("Nilo", "7788-1432"))

conexao.commit()
cursor.close()
conexao.close()
