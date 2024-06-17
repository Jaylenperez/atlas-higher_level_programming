#!/usr/bin/python3
"""
Lists all states from the database  hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

def main():
    """
    Main function to access the database and fetch the states.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Execute the query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Print each row
        for row in rows:
            print(row)
        
        # Close the cursor and connection
        cursor.close()
        db.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()