from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

connection_line = (
    'postgresql+psycopg2'
    '://'
    'sqlalch:password'
    '@'
    'localhost:5432'
    '/'
    'sqlalchdb'
)
engine = create_engine(connection_line)
session = Session(bind=engine)

Base = declarative_base()


class TaskJson(BaseModel):
    title: str
    content: str


class TaskTitle(BaseModel):
    title: str


class TaskContent(BaseModel):
    content: str


class TaskModel(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    done = Column(Boolean, default=False, nullable=False)
    done_at = Column(DateTime)


Base.metadata.create_all(engine)
