#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb as db # imports MySQLdb module, aliased as db for convenience
from sys import argv # imports argv list from the sys module, which contains the command-line arguments passed to the script.

if __name__ == "__main__": # Ensure the script runs only if it is executed directly, not if its imported as a module
    """
    Access the database to get the states.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3]) # Establish connection to the MySQL database
    db_cursor = db_connect.cursor() # Creates cursor object that can be used to execute SQL queries on the database.

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4])) # Executes SQL query to select rows where the name matches the argument; Using format to create SQL query with user input
                                                        # ORDER BY states.id ASC ensures results are sorted by the id column in ascending order.
    rows_selected = db_cursor.fetchall() # Fetches all the rows from the executed query

    for row in rows_selected:
        print(row) # Prints each row in the result set.