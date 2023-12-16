#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def del_state_a():
    """
    Delete states names containing 'a'
    """
    # Create an engine and connect to a database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query the database
    states = session.query(State).all()
    # Delete states with 'a'
    for state in states:
        if 'a' in state.name:
            session.delete(state)

    # Commit session
    session.commit()
    # Close session
    session.close()

if __name__ == "__main__":
    del_state_a()
