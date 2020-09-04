# Base node
FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Run tests to avoid build to complete if they fail
RUN pytest tests.py

CMD [ "python", "./nqueens.py" ]