# setting up the connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'



engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creation of the session tp start communicating with the table
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Mapping other class created to the base 
Base = declarative_base()
