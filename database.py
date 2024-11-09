from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_URL = "postgresql://user:password@db:5432/points_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Import models to register them with the Base
    from models import Point
    Base.metadata.create_all(bind=engine)
