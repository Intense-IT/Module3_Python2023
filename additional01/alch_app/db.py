from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'sqlite:///my_database.db'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


def init_db():
    import alch_app.models
    Base.metadata.create_all(bind=engine)
