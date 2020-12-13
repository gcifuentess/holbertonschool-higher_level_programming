#!/usr/bin/python3
'''
Query with SQLAlchemy, first State object from the database hbtn_0e_6_usa
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
    my_query = session.query(State).order_by(State.id)
    if my_query: # my_query.count() != 0:
        print("{}: {}".format(my_query[0].id, my_query[0].name))
    else:
        print("Nothing")
    session.close()
