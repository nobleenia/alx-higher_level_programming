#!/usr/bin/python3
"""
A script to connect to a MySQL server,
retrieve and print a list of cities
with their corresponding states, sorted by city ID
"""
import MySQLdb
from sys import argv

def get_cities_arg():
    """
    Connect to the MySQL server, 
    retrieve and print a list of cities
    with their corresponding states, sorted by city ID
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create a cursor
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT cities.name FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   AND states.name = '{:s}'\
                   ORDER BY cities.id ASC".format(argv[4]))

    # Fetch all rows
    rows = cursor.fetchall()
    # Create output list
    output = []

    # Print rows
    for row in rows:
        output.append(row[0])

    print(", ".join(output))

    # Close cursor and database
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Run the script if executed directly
    get_cities_arg()
