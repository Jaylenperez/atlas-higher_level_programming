#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv  # Import argv from sys to handle command-line arguments
from model_state import State, Base  # Import State and Base classes from model_state module
from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy to connect to the database
from sqlalchemy.orm import sessionmaker  # Import sessionmaker from SQLAlchemy to create a session

if __name__ == "__main__":
    """
    Access the database and add a new state
    to the database.
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

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")
    
    # Add the new State object to the session
    session.add(new_state)
    
    # Commit the session to the database
    session.commit()

    # Print the new state's id after committing to the database
    print('{0}'.format(new_state.id))
    
    # Close the session
    session.close()
