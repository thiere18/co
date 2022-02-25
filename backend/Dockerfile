  
FROM python:3.8
LABEL org.opencontainers.image.source https://github.com/sigularusrex/cura

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY pyproject.toml ./

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .