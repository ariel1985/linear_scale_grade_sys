from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Student(name={self.name})"
    
    def __str__(self):
        return f"Student(name={self.name})"
    
    def __init__(self, name='Unknown', id=None):
        super().__init__()
        self.name = name
        self.id = id
        
    # CRUD operations
        
    def create_student(self, db):
        print('Creating student : ', self.name)
        db.add(self)
        db.commit()
        db.refresh(self)
        return self
    
    def read_student(self, db):
        return db.query(Student).filter(Student.id == self.id).first()
    
    def read_all_students(self, db):
        return db.query(Student).all()
    
    def update_student(self, id, db):
        student = db.query(Student).filter(Student.id == id).first()
        student.name = self.name
        db.commit()
        return student
    
    def delete_student(self, id, db):
        student = db.query(Student).filter(Student.id == id).first()
        db.delete(student)
        db.commit()
        return student
    
## Subject 
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Subject(name={self.name})"
    
    def __str__(self):
        return f"Subject(name={self.name})"
    
    def __init__(self, name='Unknown', id=None):
        super().__init__()
        self.name = name
        self.id = id
        
    # CRUD operations
    def create_subject(self, db):
        print('Creating subject : ', self.name)
        db.add(self)
        db.commit()
        db.refresh(self)
        return self
    
    def read_all_subjects(self, db):
        return db.query(Subject).all()

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False)
    grade = Column(Integer, CheckConstraint('grade >= 0 AND grade <= 100'), nullable=False)
    
    __table_args__ = (UniqueConstraint('student_id', 'subject_id', name='unique_grade'),)
    
    def __repr__(self):
        return f"Grade(student_id={self.student_id}, subject_id={self.subject_id}, grade={self.grade})"
    
    def __str__(self):
        return f"Grade(student_id={self.student_id}, subject_id={self.subject_id}, grade={self.grade})"
    
    def __init__(self, student_id=None, subject_id=None, grade=None, id=None):
        super().__init__()
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade
        self.id = id
        
    # CRUD operations
    def create_grade(self, db):
        print('Creating grade : ', self.grade)
        db.add(self)
        db.commit()
        db.refresh(self)
        return self
    
    def read_all_grades(self, db):
        return db.query(Grade).all()
    
    def read_grade(self, db):
        return db.query(Grade).filter(Grade.id == self.id).first()
    
    def update_grade(self, id, db):
        grade = db.query(Grade).filter(Grade.id == id).first()
        grade.student_id = self.student_id
        grade.subject_id = self.subject_id
        grade.grade = self.grade
        db.commit()
        return grade
    
    def delete_grade(self, id, db):
        grade = db.query(Grade).filter(Grade.id == id).first()
        db.delete(grade)
        db.commit()
        return grade
    
    def grades_by_student(self, student_id, db):
        return db.query(Grade).filter(Grade.student_id == student_id).all()
    
    def grades_by_subject(self, subject_id, db):
        return db.query(Grade).filter(Grade.subject_id == subject_id).all()
    
    
if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    load_dotenv()
    DATABASE_URL = os.getenv('DATABASE_URL') 

    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    student = Student(name='John Doe')
    session.add(student)
    session.commit()
    
    subject = Subject(name='Math')
    session.add(subject)
    session.commit()
    
    grade = Grade(student_id=student.id, subject_id=subject.id, grade=85)
    session.add(grade)
    session.commit()
    
    session.close()
    
    print('Database tables created successfully')