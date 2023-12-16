#!/usr/bin/python3
"""
List first state from the database using SQLAlchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def list_first_state():
    """
    Connect to the database and list the first state
    """
    # Create an engine to connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query first state from the database
    first = session.query(State).first()

    if first:
        print("{first.id}: {first.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    list_first_state()
