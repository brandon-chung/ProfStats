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
    session = sessionmaker(bind=engine)
    return session

def init_db():
    """
    Initializes databases and tables.
    """
    models.Base.metadata.create_all(engine)
    

def drop_db():
    """
    Drops the database (Clears it)
    """
    models.Base.metadata.drop_all(engine)
    
def insert_item(session, item):
    """
    Given a session and item (an object of one of the classes in models), insert it into database
    """

    session.add(item)
    session.commit()

def query_prof(session, first_name, last_name) -> models.Prof:
    """
    Queries a professor based on name, then returns their ProfStat
    """
    prof = session.query(models.Prof).\
            filter(models.Prof.first_name == first_name, models.Prof.last_name == last_name).one_or_none()
    return prof