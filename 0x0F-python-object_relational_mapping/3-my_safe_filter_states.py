#!/usr/bin/python3
"""
A script to connect to a MySQL server,
retrieve and print a list of states
whose names match a provided pattern,
sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv

def get_states_no_injectn():
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

    # Create cursor
    cursor = db.cursor()

    # Execute SQL query to show all states that matches a new argument
    cursor.execute("SELECT * FROM states WHERE name='{:s}'\
                   ORDER by id ASC".format(argv[4]))

    # Fetch all rows
    rows = cursor.fetchall()
    # Print the resuls
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Run the script when executed directly
    get_states_no_injectn()
