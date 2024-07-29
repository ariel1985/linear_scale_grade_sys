# app/routes.py

from pydantic import BaseModel
from fastapi import APIRouter
from app.db_conn import SessionLocal
from app.models import Student, Subject, Grade

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Grading Service"}

#################################################
# student CRUD operations pydantic models
class CreateStudentScheme(BaseModel):
    name: str
    
class StudentScheme(BaseModel):
    id: int
    name: str
    
class StudentsScheme(BaseModel):
    students: list[StudentScheme]


### Student 

@router.post("/students/")
def create_student(data: CreateStudentScheme):
    db = SessionLocal()
    student = Student(name=data.name)
    new_student = student.create_student(db)
    print('new_student:', new_student)
    return new_student

@router.get("/students/{student_id}")
def read_student(student_id: int):
    db = SessionLocal()
    student = Student(id=student_id)
    return student.read_student(db)

@router.get("/students/")
def read_all_students():
    db = SessionLocal()
    student = Student()
    return student.read_all_students(db)

# Subject 


#################################################
# subject CRUD operations pydantic models
class CreateSubjectScheme(BaseModel):
    name: str
    
class SubjectScheme(BaseModel):
    id: int
    name: str
    
class SubjectsScheme(BaseModel):
    subjects: list[SubjectScheme]
    
@router.post("/subjects/")
def create_subject(data: CreateSubjectScheme):
    db = SessionLocal()
    subject = Subject(name=data.name)
    new_subject = subject.create_subject(db)
    print('new_subject:', new_subject)
    return new_subject

@router.get("/subjects/")
def read_all_subjects():
    db = SessionLocal()
    subject = Subject()
    return subject.read_all_subjects(db)


#################################################
# Grades
class CreateGradeScheme(BaseModel):
    student_id: int
    subject_id: int
    grade: int
    
class GradeScheme(BaseModel):
    id: int
    student_id: int
    subject_id: int
    grade: int
    
class GradesBySubjectScheme(BaseModel):
    number_of_students: int
    average_grade: float
    median_grade: float
    
class GradeDetailsScheme(BaseModel):
    subject_id: int
    grade: int
    
class GradesByStudentScheme(BaseModel):
    grades: list[GradeDetailsScheme]
    average_grade: float
    
@router.post("/grades/")
def create_grade(data: CreateGradeScheme):
    db = SessionLocal()
    grade = Grade(student_id=data.student_id, subject_id=data.subject_id, grade=data.grade)
    new_grade = grade.create_grade(db)
    print('new_grade:', new_grade)
    return new_grade

@router.get("/grades/")
def read_all_grades():
    db = SessionLocal()
    grade = Grade()
    return grade.read_all_grades(db)

# grades by subject
@router.get("/grades/subject/{subject_id}")
def read_grades_by_subject(subject_id: int):
    db = SessionLocal()
    grade = Grade()
    return grade.grades_by_subject(subject_id, db)

# grades by student
@router.get("/grades/student/{student_id}")
def read_grades_by_student(student_id: int):
    db = SessionLocal()
    grade = Grade()
    return grade.grades_by_student(student_id, db)
    