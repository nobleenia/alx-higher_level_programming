#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” from the databas
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

def create_state():
    """
    Create the state and City objects
    """
    # Create and engine and connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Build a table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Create the state and city
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Add new_city to cities table
    new_state.cities.append(new_city)

    # Add new entries to the session
    session.add(new_state)
    session.add(new_city)

    # Commit changes to session
    session.commit()

    # Close session
    session.close()

if __name__ == "__main__":
    create_state()
