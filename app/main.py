from fastapi import FastAPI
# from app.models import Base, get_db
from app.routes import router as api_router
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/grading_service"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# # load the models and create the tables in the database
# @app.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    # Terminal: uvicorn app.main:app --reload