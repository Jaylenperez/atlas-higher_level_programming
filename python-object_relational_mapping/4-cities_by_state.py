#!/usr/bin/python3
"""
This script lists all cities from database hbtn_0e_4_usa
"""
import MySQL as db
from sys import argv

if __name__ =="__main__": # Ensure script runs only if it is executed directly, not if it's imported as a module
    """
    Access the database to get the cities
    from the database
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3]) # Establish connection to the MySQL database.
    
    with db_connect.cursor() as db_cursor: # Create cursor object using a context manager to ensure proper resource management
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC") # Execute SQL query to select city and state info, joining cities and states tables
        rows_selected = db_cursor.fetchall() # Fetch all the rows from the executed query

    if rows_selected is not None: # Check if there are any rows selected
        for row in rows_selected: # Iterate over the rows in the result set
            print(row) # Print each row in the result set.
