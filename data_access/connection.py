from config import DB_OUT, DB_PATH
import sqlite3
import os

def connect(db_name):
    if DB_OUT:
        db_dir = os.path.expanduser(DB_PATH)
        db_path = os.path.join(db_dir, db_name)
    else:
        # Ruta del directorio en el que se encuentra este archivo dos niveles por encima. Es decir devuelve la ruta de la raiz del proyecto
        base_dir = os.path.dirname(os.path.dirname(__file__))
        # Ruta donde se encuentra la base de datos
        db_dir = os.path.join(base_dir, 'database')
        # Crea el directorio si no existe
        os.makedirs(db_dir, exist_ok=True)
        # Ruta de la base de datos
        db_path = os.path.join(db_dir, db_name)
    
    return sqlite3.connect(db_path)

def close(con):
    con.close()