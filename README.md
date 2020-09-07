# N-Queens-Puzzle

Python solution to the N Queens Puzzle saving data to a Postgres DB. The solution uses docker-compose to run 2 containers (one for the python app and one for the DB), and mounts a volume in the DB container to assure data persistency.

The basic algorithm was taken from https://github.com/sol-prog/N-Queens-Puzzle, which uses permutations and recursion for efficiency and was adapted to meet the challenge requirements.

Postgres user and password are passed as arguments to the container to avoid potential exposure of sensitive information.

To run the solution create a .env file to set postgres_user and postgres_password (see .env.example for more details) and run the following command: `docker-compose up --build`. It'll get solutions for the n-queens puzzle iterating over n from 8 to 13. Solutions are saved in a table in postgres DB, where the first column is the value of n and the second column is an array representing each solution.

A solution consists of a one-dimensional array where the index represents the row and the value represents the column of each queen.

Github actions has been configured to automatically execute tests on each push, tests also run in the build of python app container.