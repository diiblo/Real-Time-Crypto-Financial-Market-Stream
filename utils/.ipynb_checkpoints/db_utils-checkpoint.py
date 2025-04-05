# db_utils.py
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv
# charge les variables du fichier .env
load_dotenv()  

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

def init_database(db_name=POSTGRES_DB,db_user=POSTGRES_USER,db_password=POSTGRES_PASSWORD,db_host=POSTGRES_HOST,db_port=POSTGRES_PORT):
    # Connexion à PostgreSQL pour créer la BDD si elle n'existe pas
    conn_init = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    conn_init.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor_init = conn_init.cursor()

    cursor_init.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
    exists = cursor_init.fetchone()

    if not exists:
        cursor_init.execute(f"CREATE DATABASE {db_name}")
        print(f"✅ Base de données '{db_name}' créée.")
    else:
        print(f"ℹ️ Base de données '{db_name}' déjà existante.")

    cursor_init.close()
    conn_init.close()

    # Connexion à la base cible
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()

    return conn, cursor