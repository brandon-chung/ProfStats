"""
Boilerplate code for connecting to PostgreSQL 9.6 database.
"""
from services.config import POSTGRESQL_URL
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

engine = create_engine(POSTGRESQL_URL)
conn = engine.connect()


def get_db_session():
    """
    Returns database connection session.
    """
    #TODO

def init_db():
    """
    Initializes databases and tables.
    """
    #TODO

def drop_db():
    """
    Drops the database (Clears it)
    """
    #TODO