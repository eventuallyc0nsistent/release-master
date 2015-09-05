from models.db_connection import Base, engine

def init_db():
    import models.tables 
    Base.metadata.create_all(bind=engine)

init_db()
