import sqlite3

produtos = [
            ("Mouse", "37.00"),
            ("Teclado", "50.00"),
            ("Monitor", "120.00")
           ]

conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()

cursor.execute('''
                create table precos (
                    nome text,
                    preco text
                )
               ''')

cursor.executemany('''
                insert into precos (nome, preco)
                values(?, ?)''',
                produtos)

conexao.commit()

cursor.execute('''
                select * from precos
               ''')

resultado = cursor.fetchall()
for produto in resultado:
    print(f"Produto: {produto[0]}\nPreço: R$ {produto[1]}\n----------")

cursor.close()
conexao.close()
