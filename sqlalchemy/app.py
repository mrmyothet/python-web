# pip install sqlalchemy
# pip install psycopg2-binary

from sqlalchemy import Column, Integer, String, create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base


# conn = psycopg2.connect()

# Create an engine that connects to the database
engine = create_engine(url="postgresql://postgres:postgres@localhost:5434/ORM_Demo")
# print(engine)

# Model -> Table
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"User {self.name}, {self.age}"


Base.metadata.create_all(engine)
