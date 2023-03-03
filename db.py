from sqlite3 import *
def dbinit():
    connection = connect('main.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    connection.commit()
    connection.close()