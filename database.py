from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from sqlalchemy.exc import OperationalError
import time
# DATABASE_URL = "postgresql://myuser:NewPassword123!@db:5432/mydatabase"
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://myuser:NewPassword123!@db:5432/mydatabase')


def get_engine():
    while True:
        try:
            engine = create_engine(DATABASE_URL)
            # Try a simple query or connection test here
            engine.connect()
            break
        except OperationalError:
            print("Waiting for the database to be ready...")
            time.sleep(5)
    return engine
# engine = create_engine(DATABASE_URL)
engine=get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
