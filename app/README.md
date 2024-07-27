# Backend API 

## Setup

```bash
pip install -r requirements.txt
```

## Running the Service locally

```bash
uvicorn app.main:fapp --reload
```

## Running the Service in Docker

Only on local environment,
remove all images and containers to avoid conflicts:

```bash
docker-compose down
docker rmi $(docker images -q) -f
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

Run the following commands to build and run the Docker container:
```bash
docker build -t api .
docker run -p 8000:8000 api
```

When running locally you might need to run `export PYTHONPATH=$(pwd)`, so that the app can find the modules.

### Testing API

Testing for the API can be done using the Swagger UI at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.

## Models

The models are defined in the `models.py` file. The models are as follows:

- Student
- Subject
- Grade

The models are defined using SQLAlchemy ORM. The models are used to create the database schema.

### Testing the models

The models can be tested by running the following command:

```bash
pytest test_models.py
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


