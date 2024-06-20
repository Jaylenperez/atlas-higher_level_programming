#!/usr/bin/python3  # Specify the script should be run with Python 3 interpreter
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv  # Import argv from sys to handle command-line arguments
from model_state import State, Base  # Import State and Base classes from model_state module
from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy to connect to the database
from sqlalchemy.orm import sessionmaker  # Import sessionmaker from SQLAlchemy to create a session

if __name__ == "__main__":  # Ensure this block runs only if the script is executed directly
    """
    Deletes State objects in the database.
    """

    # Construct the database URL from command-line arguments
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create an engine that connects to the MySQL database
    engine = create_engine(db_url)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database to get all State objects with a name containing the letter 'a'
    states = session.query(State).filter(State.name.contains('a'))
    
    # Check if any such states exist
    if states is not None:
        # Iterate over each state object in the result
        for state in states:
            # Delete the state object from the session
            session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
