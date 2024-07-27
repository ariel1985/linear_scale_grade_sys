# app/db/db_connection.py

# app/db/db_connection.py
import os
import dotenv
from sqlalchemy import create_engine, orm, MetaData
from sqlalchemy.ext.declarative import declarative_base
# import models to create tables
from app.models import Base, Student, Subject, Grade

# Load environment variables safely
dotenv.load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
print('DATABASE_URL:', DATABASE_URL)

# Define a base class for declarative class definitions
Base = declarative_base()

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create all tables in the engine
metadata = MetaData()
metadata.create_all(engine)

# Create a configured "Session" class
SessionLocal = orm.sessionmaker(bind=engine)

# Function to get a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        