#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects, contained in the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

def list_states_cities():
    """
    Query database to list the States and the Cities beneath them
    """
    # Create an engine and connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create table if doesn't exist
    Base.metadata.create_all(engine)

    # Create session
    session = Session(engine)

    # Query the database
    states = session.query(State).order_by(State.id).all()
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    list_states_cities()
