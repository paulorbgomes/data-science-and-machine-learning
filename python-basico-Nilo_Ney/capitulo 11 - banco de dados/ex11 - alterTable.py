# alter table ...

import sqlite3

conexao = sqlite3.connect("estados.db")
cursor = conexao.cursor()

# alter table ...
# OBS: O SQLite altera somente um campo de cada vez ...
'''
cursor.execute("""
                alter table estados add sigla text
               """)

cursor.execute("""
                alter table estados add regiao text
               """)
'''

# update ...
cursor.execute("""
                update estados set sigla = 'SP' where nome = 'São Paulo'
               """)
cursor.execute("""
                update estados set regiao = 'SE' where nome = 'São Paulo'
               """)
cursor.execute("""
                update estados set sigla = 'MG' where nome = 'Minas Gerais'
               """)
cursor.execute("""
                update estados set regiao = 'SE' where nome = 'Minas Gerais'
               """)
conexao.commit()

# insert into ...
cursor.execute("""
                insert into estados (nome, populacao, sigla, regiao)
                values(?, ?, ?, ?)""",("Ceará", 0, "CE", "NE"))

# update ...
cursor.execute("""
                update estados set populacao = '8778575' where sigla = 'CE'
               """)

# select ...
cursor.execute("""
                select * from estados
               """)
consulta = cursor.fetchall()
for i in consulta:
    print(i)


cursor.close()
conexao.close()
