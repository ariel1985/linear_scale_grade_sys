from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False)
    grade = Column(Integer, CheckConstraint('grade >= 0 AND grade <= 100'), nullable=False)
    
    __table_args__ = (UniqueConstraint('student_id', 'subject_id', name='unique_grade'),)

def get_db():
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/grading_service"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
