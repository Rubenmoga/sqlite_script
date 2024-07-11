from database.connection import connect, close
import sqlite3
import csv
import os

def import_csv(db_name, table_name,csv_name):

    file_path = os.path.expanduser(f'~/Descargas/{csv_name}')

    if not os.path.isfile(file_path):
        print('El archivo csv no existe.')
        exit(1)

    # Conecta con la base de datos y si no existe la crea
    con = connect(db_table)
    cur = con.cursor()

    cur.execute(f'''CREATE TABLE IF NOT EXIST "{table_name}"(
            ID INTEGER PRIMARY key AUTOINCREMENT,
            Nombre TEXT,
            Nota REAL,
            Director TEXT,
            Tipo TEXT
            )
    ''')


    with open(csv_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            cur.execute(f'INSERT INTO "{table_name}" (Nombre, Nota, Director, Tipo) VALUES (?, ?, ?, ?)', row)

        con.commit()
        close(con)