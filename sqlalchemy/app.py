# pip install sqlalchemy
# pip install psycopg2-binary

from sqlalchemy import Column, Integer, String, create_engine
import psycopg2

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


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

Session = sessionmaker(bind=engine)
session = Session()

users = [
    ("Aung Aung", 12),
    ("Maung Maung", 22),
    ("Hla Hla", 32),
    ("Mya Mya", 42),
    ("Ko Ko", 52),
]


# for name, age in users:
#     new_user = User(name=name, age=age)
#     session.add(new_user)
#     print(f"New User added successfully: {name}, {age}")

# Create a new user
# "INSERT INTO users (name, age) VALUES ('John', 25)"
# new_user = User(name="Myo Thet", age=38)
# session.add(new_user)

session.commit()
# SELECT * FROM users
users = session.query(User).all()
print(type(users))
for user in users:
    # print(type(user))
    print(user)

# Filter
user = session.query(User).filter_by(name="Aung Aung").first()
print(user)

# Update
user = session.query(User).filter_by(name="Aung Aung").first()
user.age = 27
session.commit()
print(user)
