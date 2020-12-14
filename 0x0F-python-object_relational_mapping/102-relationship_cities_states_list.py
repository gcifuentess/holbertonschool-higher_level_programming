#!/usr/bin/python3
"""Query with SQLAlchemy, lists all City objects
from the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           encoding='utf-8', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    my_query = session.query(City).order_by(City.id)
    for city in my_query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
