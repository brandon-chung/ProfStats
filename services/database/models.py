"""
Models for database schema
"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

PROF_TABLE = 'prof'
PROF_STATS_TABLE = 'prof_stats'

Base = declarative_base()

def generate_uuid() -> str:
    """
    Generate and return uuid.
    """
    return str(uuid.uuid4())

class Prof(Base):
    __tablename__ = PROF_TABLE
    prof_id = Column(String(64), primary_key=True, default=generate_uuid)
    url = Column(String(100))
    first_name = Column(String(64))
    last_name = Column(String(64))
    rating = Column(String(64))
    average_passing = Column(String(64))
    take_again = Column(String(64))
    # Attributes
    # Follow template:
    # {Attribute_name} = Column(String({0<n<256}))

    def __init__(self, url, first_name, last_name, rating, average_passing, take_again):
        self.prof_id = generate_uuid
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.average_passing = average_passing
        self.take_again = take_again





    #prof_stats = relationship('ProfStats', back_populates=PROF_TABLE)

"""
class ProfStats(Base):
    __tablename__ = PROF_STATS_TABLE
    prof_stat_id = Column(Integer, primary_key=True, default=generate_uuid)
    prof_id = Column(String(64), ForeignKey(f'{PROF_TABLE}.prof_id'), nullable=False)

    # Attributes
    # Follow template:
    # {Attribute_name} = Column(String({0<n<256}))

    prof = relationship('Prof', back_populates=PROF_STATS_TABLE)    

"""