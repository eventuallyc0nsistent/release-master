from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from helpers.config_reader import DB_NAME, GLOBAL_PATH


# setup sqlalchemy
engine = create_engine('sqlite:///'+GLOBAL_PATH+DB_NAME+'.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
