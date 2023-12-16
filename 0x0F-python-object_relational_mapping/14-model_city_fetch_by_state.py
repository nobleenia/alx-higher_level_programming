#!/usr/bin/python3
"""
Prints all City objects from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

def fetch_cities():
    """
    Query database to print all Cities
    """
    # Create engine and connect to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query the database
    states_cities = session.query(State, City).join(City).all()
    #Print the results
    for state, city in states_cities:
        print(f"{state.name}: ({state.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    fetch_cities()
