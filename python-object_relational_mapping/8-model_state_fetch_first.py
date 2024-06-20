#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv # import argv to handle command-line arguments
from model_state import State, Base # Import State and Base from model_state module
from sqlalchemy import create_engine # Import create_engine for database connection
from sqlalchemy.orm import sessionmaker # Import sessionmaker to create a session

if __name__ == "__main__": # Check if the script is being run directly
    """
    Access to the database and get a state
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

    # Query the database to get the first State object, ordered by its id
    state = session.query(State).order_by(State.id).first()
    # Check if the state was found
    if state is not None:
        # Print the id and name of the first State object
        print('{0}: {1}'.format(state.id, state.name))
    else:
        # Print 'Nothing' if no State object was found
        print("Nothing")