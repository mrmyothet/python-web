import psycopg2
from psycopg2 import sql


def get_db():
    conn = psycopg2.connect(
        dbname="Blog",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5434",
    )
    return conn


def get_sqlite3_db():
    pass
