#!/usr/bin/python3
"""
This script defines a State class and a
base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String # import necessary classes from SQLAlchemy module
from sqlalchemy.ext.declarative import declarative_base # importing declarative_base function from SQLAlchemy module

Base = declarative_base() # Create a base class for declaritive class definitions


class State(Base):
    """
    State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states' # name of the table in the database

    id = Column(Integer, primary_key=True) # Primary key column for the State class
    name = Column(String(128), nullable=False) # Column to store the name of the state