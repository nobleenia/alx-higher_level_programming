#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def add_state_obj():
    """
    Add a State object to the database and print its ID
    """
    # Create engine and connect to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Create new state
    new_state = State(name='Louisiana')
    
    # Add object to the database
    session.add(new_state)
    # Commit the change
    session.commit()
    print(new_state.id)

    # Close the session
    session.close()

if __name__ == "__main__":
    add_state_obj()
