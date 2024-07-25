import pytest
from fastapi.testclient import TestClient
from main import app
from models import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/grading_service"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data

def test_create_subject():
    response = client.post("/subjects/", json={"name": "Math"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Math"
    assert "id" in data

def test_submit_grade():
    student_response = client.post("/students/", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    subject_response = client.post("/subjects/", json={"name": "Math"})
    subject_id = subject_response.json()["id"]

    response = client.post("/grades/", json={"student_id": student_id, "subject_id": subject_id, "grade": 85})
    assert response.status_code == 201
    assert response.json() == {"message": "Grade submitted successfully"}

def test_get_grades_by_subject():
    student_response = client.post("/students/", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    subject_response = client.post("/subjects/", json={"name": "Math"})
    subject_id = subject_response.json()["id"]

    client.post("/grades/", json={"student_id": student_id, "subject_id": subject_id, "grade": 85})

    response = client.get(f"/grades/subject/{subject_id}")
    assert response.status_code == 200
    data = response.json()
    assert "number_of_students" in data
    assert "average_grade" in data
    assert "median_grade" in data

def test_get_grades_by_student():
    student_response = client.post("/students/", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    subject_response = client.post("/subjects/", json={"name": "Math"})
    subject_id = subject_response.json()["id"]

    client.post("/grades/", json={"student_id": student_id, "subject_id": subject_id, "grade": 85})

    response = client.get(f"/grades/student/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert "grades" in data
    assert "average_grade" in data
