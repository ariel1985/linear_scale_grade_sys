# Linear Scale Grade Service

This is a simple service that provides a RESTful API for managing student grades in a school. The service is built using Python and FastAPI, and it uses a PostgreSQL database to store student, subject, and grade information.


## Requirements

- Python 3.10
- Docker
- Docker Compose

## Installation

1. Clone the repository:

```bash
git clone git@github.com:ariel1985/linear_scale_grade_sys.git
```

2. Change into the project directory:

```bash
cd linear-scale-grade-service
```

3. Create a `.env` file in the project root directory with the following environment variables:

```bash
DATABASE_URL=postgresql://postgres:postgres@db/postgres
```

4. Build and start the Docker containers:

```bash
docker-compose up --build

# or use the load balancer acting as linear scale
docker-compose up --scale api=3
```

Note: To sync between the database and API service, the loading time takes about 10 seconds.

5. The service should now be running at `http://localhost:8000`.

To view the API documentation, navigate to `http://localhost:8000/docs`.


## Linear Scale Grade Service

Load Balancer Acting as Linear Scale
The Nginx load balancer allows horizontal scaling by distributing incoming HTTP requests across multiple instances of the FastAPI application. Here’s how it works:

Upstream Servers:

The upstream block in the nginx.conf file defines a group of servers (api_servers). Requests to the load balancer are distributed among these servers.
Currently, it points to a single instance (api:8000). For true horizontal scaling, you can deploy multiple instances of the FastAPI application.
Load Balancing:

Nginx balances the incoming traffic across the defined upstream servers. This means if you scale the api service to multiple replicas, Nginx will distribute the traffic among them.


### To use: 

```bash
docker-compose up --scale api=3
```