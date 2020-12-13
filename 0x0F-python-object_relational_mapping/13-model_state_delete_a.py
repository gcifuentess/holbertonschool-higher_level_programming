#!/usr/bin/python3
'''
Query with SQLAlchemy,deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           encoding='utf-8', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    to_delete = session.query(State).filter(State.name.like('%a%'))
    for state in to_delete:
        session.delete(state)
    session.commit()
    session.close()
