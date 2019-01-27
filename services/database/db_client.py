"""
Boilerplate code for connecting to PostgreSQL 9.6 database.
"""
from sqlalchemy import create_engine, not_
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session