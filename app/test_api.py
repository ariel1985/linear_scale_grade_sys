import json

def test_create_student(client):
    response = client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data

def test_create_subject(client):
    response = client.post("/subjects/", json={"name": "Math"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Math"
    assert "id" in data

def test_submit_grade(client):
    # Add a student and subject first
    student_response = client.post("/students/", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    subject_response = client.post("/subjects/", json={"name": "Math"})
    subject_id = subject_response.json()["id"]

    # Submit a grade
    response = client.post("/grades/", json={
        "student_id": student_id,
        "subject_id": subject_id,
        "grade": 85
    })
    assert response.status_code == 201
    assert response.json() == {"message": "Grade submitted successfully"}

def test_get_grades_by_subject(client):
    # Add a student and subject first
    student_response = client.post("/students/", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    subject_response = client.post("/subjects/", json={"name": "Math"})
    subject_id = subject_response.json()["id"]

    # Submit a grade
    client.post("/grades/", json={
        "student_id": student_id,
        "subject_id": subject_id,
        "grade": 85
    })

    # Retrieve grades by subject
    response = client.get(f"/grades/subject/{subject_id}")
    assert response.status_code == 200
    data = response.json()
    assert "number_of_students" in data
    assert "average_grade" in data
    assert "median_grade" in data

def test_get_grades_by_student(client):
    # Add a student and subject first
    student_response = client.post("/students/", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    subject_response = client.post("/subjects/", json={"name": "Math"})
    subject_id = subject_response.json()["id"]

    # Submit a grade
    client.post("/grades/", json={
        "student_id": student_id,
        "subject_id": subject_id,
        "grade": 85
    })

    # Retrieve grades by student
    response = client.get(f"/grades/student/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert "grades" in data
    assert "average_grade" in data
