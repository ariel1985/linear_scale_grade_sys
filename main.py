from fastapi import FastAPI
from app.routes import router as api_router
from app.db_conn import SessionLocal

app = FastAPI()
app.include_router(api_router)

# Terminal: uvicorn app.main:app --reload

if __name__ == "__main__":
    import os
    import dotenv
    from sqlalchemy.ext.declarative import declarative_base
    # import models to create tables
    from app.models import Base, Student, Subject, Grade
    from sqlalchemy import create_engine, orm, MetaData
    
    # Load environment variables safely
    dotenv.load_dotenv('.env')

    DATABASE_URL = os.getenv('DATABASE_URL')
    print('DATABASE_URL:', DATABASE_URL)

    # Define a base class for declarative class definitions
    Base = declarative_base()

    # Create an engine
    engine = create_engine(DATABASE_URL, echo=True)

    # Create all tables in the engine
    metadata = MetaData()
    metadata.create_all(engine)


    