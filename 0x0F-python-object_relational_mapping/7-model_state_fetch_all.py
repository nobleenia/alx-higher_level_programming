#!/usr/bin/python3
"""
List all states from the database using SQLAlchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def list_state():
    """
    Connect to the database and list all states
    """
    # Create an engine to connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),pool_pre_ping=True)

    # Create the tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query all states from the database
    rows = session.query(State).all()

    # Print the list of states
    for row in rows:
        print(f"{row.id}: {row.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    list_state()
