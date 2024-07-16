from .connection import connect, close
import sqlite3

def create_table(db_name, table_name):
    con = connect(db_name)
    cur = con.cursor()

    cur.execute(f'''CREATE TABLE IF NOT EXISTS "{table_name}"(
            ID INTEGER PRIMARY key AUTOINCREMENT,
            Nombre TEXT,
            Nota REAL,
            Director TEXT,
            Tipo TEXT
            )
    ''')

    con.commit()
    close(con)


def isert_row(db_name, table_name, new_row):
    con = connect(db_name)
    cur = con.cursor()

    new_row = new_row.split(',')
            
    cur.execute(f'INSERT INTO "{table_name}" (Nombre, Nota, Director, Tipo) VALUES (?,?,?,?)',new_row)

    con.commit()
    close(con)


def delete_row(db_name, table_name, id_row):
    con = connect(db_name)
    cur = con.cursor()

    cur.execute(f'DELETE FROM "{table_name}" WHERE ID={id_row}')

    con.commit()
    close()


def table_exists(db_name, table_name):
    con = connect(db_name)
    cur = con.cursor()

    cur.execute(f'''SELECT "{table_name}" FROM sqlite_master WHERE type = 'table' ''')
    result = cur.fetchone()

    return result