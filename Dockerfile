# Dockerfile for python app
FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python", "./nqueens.py" ]