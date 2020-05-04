from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from ..config import database_path

engine = create_engine(database_path)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

from .models import *

Base.metadata.create_all(engine)
session = Session()
