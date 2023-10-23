from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine("postgresql://postgres:postgres@localhost:9999/postgres")

__session = sessionmaker(engine)
session: Session = __session()