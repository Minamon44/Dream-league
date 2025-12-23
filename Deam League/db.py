import psycopg2
from flask import g
from config import Config

DATABASE_URL = "postgresql://postgres:1182003@localhost:5432/postgres"

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(DATABASE_URL)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
