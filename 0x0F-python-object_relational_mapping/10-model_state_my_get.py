#!/usr/bin/python3
"""
A script that prints the State object with the specified name from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_state_name():
    """
    Print the State object with the specified name from the database
    """
    # Create an engine and connect to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2], argv[3]), pool_pre_ping=True)

    # Create tables if doesn't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query the states with the name passed
    state = session.query(State).filter(State.name == argv[4]).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    list_state_name()
