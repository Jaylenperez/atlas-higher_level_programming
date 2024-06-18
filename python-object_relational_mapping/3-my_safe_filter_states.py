#!/usr/bin/python3
"""
This is a script that takes in arguments
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
that is safe from MySQL injections.
"""
import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access database to get the states.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3]) # Establish connection to MySQL database.

    db_cursor = db_connect.cursor() # Creates cursor object that can be used to execute SQL queries on the database.
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]}) # Execute SQL query to select rows where the name matches the argument, using paramerterized query to prevent SQL injection.

    rows_selected = db_cursor.fetchall() # Fetches all the rows from the executed query

    for row in rows_selected:
        print(row) # Prints each row in the result set.
