# Dockerfile for python app
FROM python:3

WORKDIR /usr/src/app

COPY . .

ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pytest tests.py

CMD [ "python", "./nqueens.py" ]