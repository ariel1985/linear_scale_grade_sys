# docker file for fastapi app

# base image
FROM python:3.8-slim

# set working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# copy project
COPY . /app

# uvicorn main:app --reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t api .
# docker run --name api -p 8000:8000 api