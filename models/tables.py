from models.db_connection import Base
from sqlalchemy import create_engine, Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    github_access_token = Column(String(200))

    def __init__(self, username, github_access_token):
        self.username = username
        self.github_access_token = github_access_token
