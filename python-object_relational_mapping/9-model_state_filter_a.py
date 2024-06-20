#!/usr/bin/python3  # Shebang line to indicate the script should be run with Python 3
"""
This script lists all State objects
that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv  # Import argv to handle command-line arguments
from model_state import State, Base  # Import State and Base from model_state module
from sqlalchemy import create_engine  # Import create_engine for database connection
from sqlalchemy.orm import sessionmaker  # Import sessionmaker to create a session

if __name__ == "__main__":  # Check if the script is being run directly
    """
    Access to the database and get states
    from the database.
    """

    # Construct the database URL using command-line arguments for user, password, and database name
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create an engine object based on the constructed database URL
    engine = create_engine(db_url)
    
    # Bind the engine to the sessionmaker to create a configured Session class
    Session = sessionmaker(bind=engine)

    # Instantiate a Session object to interact with the database
    session = Session()

    # Query the database to get all State objects whose name contains the letter 'a'
    states = session.query(State).filter(State.name.contains('a'))
    
    # Check if any states were found
    if states is not None:
        # Iterate through each state in the query result
        for state in states:
            # Print the id and name of each State object
            print('{0}: {1}'.format(state.id, state.name))
