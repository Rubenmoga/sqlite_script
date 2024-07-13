#!/usr/bin/env python3

from config import DB_NAME
import argparse
from data_access.operation import isert_row, create_table
from data_access.fetch import fetch
from utils.import_csv import import_csv

def main():

    parser = argparse.ArgumentParser(
                    prog = 'Peliculas',
                    description = 'Un pequeño programam para almacenaje y manejo de una base de datos de peliculas '
    )

    parser.add_argument('table_name', type=str, help='Nombre de la tabla sobre la que quiero actuar')
    parser.add_argument('-n', '--new', action='store', help= 'Añadir una nueva linea a una tabla')
    parser.add_argument('-nt', '--newtable',action='store_true', help='Crea una nueva tabla en la base de datos con el nombre de table_name')
    parser.add_argument('-icsv', '--importcsv', action='store',nargs=1, help='Importa los datos de un csv en una nueva o ya existente base de datos')

    args = parser.parse_args()
   
    if args.new:
        isert_row(DB_NAME, args.table_name, args.new)
    elif args.newtable:
        create_table(DB_NAME, args.table_name)
    elif args.importcsv:
        import_csv(DB_NAME, args.table_name, args.importcsv[0])
    else:
        fetch(DB_NAME, args.table_name)




if __name__ == '__main__':
    main()