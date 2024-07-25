from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from models import Student, Subject, Grade, get_db

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Grading Service"}

# @router.post("/students/", response_model=Student)
# def create_student(name: str, db: Session = Depends(get_db)):
#     student = Student(name=name)
#     db.add(student)
#     db.commit()
#     db.refresh(student)
#     return student

# @router.post("/subjects/", response_model=Subject)
# def create_subject(name: str, db: Session = Depends(get_db)):
#     subject = Subject(name=name)
#     db.add(subject)
#     db.commit()
#     db.refresh(subject)
#     return subject

# @router.post("/grades/")
# def submit_grade(student_id: int, subject_id: int, grade: int, db: Session = Depends(get_db)):
#     grade_entry = db.query(Grade).filter(Grade.student_id == student_id, Grade.subject_id == subject_id).first()
#     if grade_entry:
#         grade_entry.grade = grade
#     else:
#         grade_entry = Grade(student_id=student_id, subject_id=subject_id, grade=grade)
#         db.add(grade_entry)
#     db.commit()
#     return {"message": "Grade submitted successfully"}

# @router.get("/grades/subject/{subject_id}")
# def get_grades_by_subject(subject_id: int, db: Session = Depends(get_db)):
#     grades = db.query(Grade).filter(Grade.subject_id == subject_id).all()
#     if not grades:
#         raise HTTPException(status_code=404, detail="Subject not found")
#     grades_list = [grade.grade for grade in grades]
#     return {
#         "number_of_students": len(grades_list),
#         "average_grade": sum(grades_list) / len(grades_list) if grades_list else 0,
#         "median_grade": sorted(grades_list)[len(grades_list) // 2] if grades_list else 0
#     }

# @router.get("/grades/student/{student_id}")
# def get_grades_by_student(student_id: int, db: Session = Depends(get_db)):
#     grades = db.query(Grade).filter(Grade.student_id == student_id).all()
#     if not grades:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return {
#         "grades": [{"subject_id": grade.subject_id, "grade": grade.grade} for grade in grades],
#         "average_grade": sum(grade.grade for grade in grades) / len(grades) if grades else 0
#     }
