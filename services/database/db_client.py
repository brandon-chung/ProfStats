"""
Boilerplate code for connecting to PostgreSQL 9.6 database.
"""
from services.config import POSTGRESQL_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.database import models


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
    models.Base.metadata.create_all(engine)
    #TODO

def drop_db():
    """
    Drops the database (Clears it)
    """
    models.Base.metadata.drop_all(engine)
    #TODO