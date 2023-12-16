#!/usr/bin/python3
"""
Changes the name of a State object from the database 
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def change_list_name():
    """
    Change the name of a specific state id
    """
    # Create an engine and connect to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create the table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query the database to find id to change
    state_to_change = session.query(State).filter(State.id == 2).first()
    # Change the state name
    state_to_change.name = "New Mexico"

    # Commit the change
    session.commit()
    
    # Close the session
    session.close()

if __name__ == "__main__":
    change_list_name()
