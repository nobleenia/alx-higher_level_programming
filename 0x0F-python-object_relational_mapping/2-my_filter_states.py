#!/usr/bin/python3
"""
A script to connect to a MySQL server,
retrieve and print a list of states
whose names match a provided pattern,
sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv

def get_states_arg():
    """
    Connect to the MySQL server, retrieve and print a list of states
    whose names match the provided pattern, sorted by states.id
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create a cursor
    cursor = db.cursor()

    # Execute the SQL query to select states with a name pattern and order by id
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}'\
                    ORDER BY id ASC".format(argv[4]))

    # Fetch all rows
    rows = cursor.fetchall()
    # Print the results
    for i in rows:
        print(i)

    # Close cursor and database
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Run the script when executed directly
    get_states_arg()
