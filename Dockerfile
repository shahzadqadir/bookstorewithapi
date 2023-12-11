# pull docker iamge
FROM python:3.10

# setup environment
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /code

# copy dependencies files
COPY Pipfile Pipfile.lock /code/

# install dependencies
RUN pip install pipenv && pipenv install --system

# copy rest of project files
COPY . /code/