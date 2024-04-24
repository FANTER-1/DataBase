from flask import g
import psycopg2
import psycopg2.extras

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname='your_dbname',
            user='your_username',
            password='your_password',
            host='your_host'
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
