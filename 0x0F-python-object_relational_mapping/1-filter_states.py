#!/usr/bin/python3
"""
A script to connect to a MySQL server,
retrieve and print a list of states
whose names start with the letter 'N' (case-sensitive),
sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv

def get_n_states():
    """
    Connect to the MySQL server, retrieve and print a list of states
    whose names start with the letter 'N', sorted by states.id
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    
    # Create a cursor
    cursor = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the results
    for i in rows:
        print(i)

    # Close the cursor and database
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Run the script when executed directly
    get_n_states()
