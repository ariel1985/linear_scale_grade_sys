from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class Students(StudentBase):
    students: List[Student]

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int

    class Config:
        orm_mode = True

class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    grade: int

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    id: int

    class Config:
        orm_mode = True

class GradesBySubject(BaseModel):
    number_of_students: int
    average_grade: float
    median_grade: float

class GradeDetails(BaseModel):
    subject_id: int
    grade: int

class GradesByStudent(BaseModel):
    grades: List[GradeDetails]
    average_grade: float
