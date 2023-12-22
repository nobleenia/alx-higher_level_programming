#!/usr/bin/python3
"""
A script to connect to a MySQL server,
retrieve and print a list of cities
with their corresponding states, sorted by city ID
"""
import MySQLdb
from sys import argv


def get_cities():
    """
    Connect to the MySQL server,
    retrieve and print a list of cities
    with their corresponding states, sorted by city ID
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    get_cities()
