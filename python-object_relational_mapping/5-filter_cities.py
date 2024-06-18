#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb as db
from sys import argv

if __name__ == "__main__": # Ensure script runs only if it is executed directly, not if its imported as a module
    """
    Access the database to get states
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3]) # Establish a connection to the MySQL database.

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4] # Pass the state name as a parameter to prevent SQL injection
        })
        rows_selected = db_cursor.fetchall() # Fetch all the rows from the executed query

    if rows_selected is not None: # Check if any rows were selected
        print(", ".join([row[1] for row in rows_selected])) # print the name of cities, joining them with commas