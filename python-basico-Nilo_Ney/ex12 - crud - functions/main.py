'''
SQLite CRUD ...
'''

import sqlite3

def create_db():
    global conexao, cursor
    conexao = sqlite3.connect("students.db")
    cursor = conexao.cursor()

def close_db():
    cursor.close()
    conexao.close()

def create_table():
    cursor.execute('''
                    create table students (
                        id integer primary key autoincrement,
                        name text,
                        course text
                    )
                   ''')

def insert_into():
    cursor.execute('''
                    insert into students (name, course)
                    values(?, ?)''',
                   ("Ricardo", "JavaScript"))
    conexao.commit()

def select_all():
    cursor.execute('''
                    select * from students
                   ''')
    result = cursor.fetchall()
    for item in result:
        print(f"Id: {item[0]}; Name: {item[1]}; Course: {item[2]}")

def select_where():
    cursor.execute('''
                    select * from students where name = "Ricardo"
                   ''')
    result = cursor.fetchall()
    for item in result:
        print(f"Id: {item[0]}; Name: {item[1]}; Course: {item[2]}")

def update_where():
    cursor.execute('''
                    update students set name = "Paulo R. B. Gomes" where id = "1"
                   ''')
    conexao.commit()

def delete_where():
    cursor.execute('''
                    delete from students where course = "JavaScript"
                   ''')
    conexao.commit()

if __name__ == "__main__":
    # Crud (CREATE) ...
    # create database ...
    create_db()

    # create table ...
    '''
    create_table()
    '''

    # insert into ...
    insert_into()

    # cRud (READ) ...
    select_all()
    '''
    select_where()
    '''

    # crUd (UPDATE) ...
    '''
    update_where()
    select_all()
    '''

    # cruD (DELETE) ...
    '''
    delete_where()
    select_all()
    '''
    
    # close db ...
    close_db()





    

    
