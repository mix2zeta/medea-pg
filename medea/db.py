import sys

from conf import setting
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def init_app_db():
    print('init db')
    with connect(user='postgres', host = 'pg-db') as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        curr = connection.cursor()
        curr.execute(f'DROP DATABASE IF EXISTS "{setting.PGDBNAME}"')
        curr.execute(f'CREATE DATABASE "{setting.PGDBNAME}"')
        curr.execute(f'CREATE SCHEMA IF NOT EXISTS medea')
        curr.execute('''
        CREATE TABLE medea.migration (
            id SERIAL,
            migration_name TEXT NOT NULL UNIQUE,
            created TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            PRIMARY KEY (id)
        );
        ''')
        curr.close()
