from .config import DB_NAME
import argparse

def main():

    parser = argparse.ArgumentParser(
                    prog = 'Peliculas',
                    description = 'Un pequeño programam para almacenaje y manejo de una base de datos de peliculas '
    )

    parser.add_argument('filename')
    parser.add_argument('table_name', type=str, help='Nombre de la tabla sobre la que quiero actuar')
    parser.add_argument('-n', '--new', action='store', help= 'Añadir una nueva linea a una tabla') # Añadir a posteriori la multiple adición con nargs='+'
    parser.add_argument('-nt', '-newtable', help='Crea una nueva tabla en la base de datos con el nombre de table_name')
    parser.add_argument('-icsv', '--importcsv', action='store',nargs=1, help='Importa los datos de un csv en una nueva o ya existente base de datos')











if __name__ == '__main__':
    main()