import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
import sqlmodel

load_dotenv()

database_url = os.getenv("database_url")

engine = create_engine(database_url, echo=True)

sqlmodel.MetaData.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
