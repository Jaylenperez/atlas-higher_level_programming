#!/usr/bin/python3  # Specify the script should be run with Python 3 interpreter
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv  # Import argv from sys to handle command-line arguments
from model_state import State, Base  # Import State and Base classes from model_state module
from model_city import City  # Import City class from model_city module
from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy to connect to the database
from sqlalchemy.orm import sessionmaker  # Import sessionmaker from SQLAlchemy to create a session

if __name__ == "__main__":  # Ensure this block runs only if the script is executed directly
    """
    Access the database and get the cities
    from the database.
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

    # Query the database to get all City objects and their associated State objects using join
    results = session.query(City, State).join(State)

    # Iterate over each pair of city and state in the result
    for city, state in results.all():
        # Print the state's name, city's id, and city's name
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Commit the session to the database (not necessary for read-only operations, but included)
    session.commit()
    
    # Close the session
    session.close()
