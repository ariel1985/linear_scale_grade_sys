# Backend API 

## Setup

```bash
pip install -r requirements.txt
```

## Running the Service

```bash
uvicorn app.main:app --reload
```

## Testing

```bash
pytest
```



## Database Schema

Use Alchemy to generate the schema from the models.


## API Endpoints

Below is a table of the API endpoints available in the backend service.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/students/` | `POST` | Creates a new student. |
| `/students/` | `GET` | Retrieves a list of all students. |
| `/subjects/` | `POST` | Creates a new subject. |
| `/subjects/` | `GET` | Retrieves a list of all subjects. |
| `/grades/` | `POST` | Submits a grade for a student in a subject. |
| `/grades/subject/{subject_id}` | `GET` | Retrieves grades for a specific subject. |
| `/grades/student/{student_id}` | `GET` | Retrieves grades for a specific student in all subjects. |


