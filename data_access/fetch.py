import sqlite3
from .connection import connect, close
from .operation import table_exists
#from prettytable.colortable import ColorTable, Themes
from prettytable import PrettyTable


def fetch(db_name, table_name):

    #tabla = ColorTable(theme=Themes.OCEAN)
    tabla = PrettyTable() # Inicilizo la variable tabla
    
    con = connect(db_name)
    cur = con.cursor()

    if not table_exists(db_name, table_name):
        print('La tabla no existe.')
        exit(1)

    cur.execute(f'SELECT * FROM "{table_name}"')

    nom_columnas = [description[0] for description in cur.description]

    # Agrego el nombre de las columnas
    tabla.field_names = nom_columnas

    for row in cur.fetchall():
        tabla.add_row(row)

    tabla.align[nom_columnas[1]]='l' # Alineo la primera y tercera columna a la izquierda
    tabla.align[nom_columnas[3]]='l'

    print(tabla)

    close(con)