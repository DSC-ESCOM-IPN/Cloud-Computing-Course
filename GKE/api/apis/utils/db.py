import os
from sqlalchemy import create_engine 

def getconn():
    db = create_engine(f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASS"]}@localhost:5432/{os.environ["POSTGRES_DB"]}')
    return db.connect()