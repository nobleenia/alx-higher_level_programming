#!/usr/bin/python3
"""
List all states containing 'a' from the database using SQLAlchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def state_filter():
    """
    Filter and print states containing the letter 'a'
    """
    # Create an engine and connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2], argv[3]), pool_pre_ping=True)

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query states containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    state_filter()
