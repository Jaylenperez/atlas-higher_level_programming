#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv # Import argv to handle command-line arguments
from model_state import State, Base # Import State and Base from model_state module
from sqlalchemy import create_engine # Import create_engine for database connection
from sqlalchemy.orm import sessionmaker # Import sessionmaker to create a session

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]) # Construct the database URL using command-line arguments

    engine = create_engine(db_url) # Create an engine object based on the database URL
    Session = sessionmaker(bind=engine) # Bind the engine to the sessionmaker to esablish a session

    session = Session() # Instantiate a Session

    for instance in session.query(State).order_by(State.id): # Query the database to get all State objects, ordered by their id
        print('{0}: {1}'.format(instance.id, instance.name)) # Print each State object's id and name