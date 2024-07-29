# Linear Scale Grade Service

This is a simple service that provides a RESTful API for managing student grades in a school. The service is built using Python and FastAPI, and it uses a PostgreSQL database to store student, subject, and grade information.


## Requirements

- Python 3.10
- Docker
- Docker Compose

## Installation

1. Clone the repository:

```bash
git clone
```

2. Change into the project directory:

```bash
cd linear-scale-grade-service
```

3. Create a `.env` file in the project root directory with the following environment variables:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

4. Build and start the Docker containers:

```bash
docker-compose up --build
```

5. The service should now be running at `http://localhost:8000`.

## API Endpoints
