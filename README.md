# N-Queens-Puzzle

Python solution to the N Queens Puzzle saving data to a Postgres DB. The solution uses docker-compose to run 2 containers (one for the python app and one for the DB), and mounts a volume in the DB container to assure data persistency.

The core solution of the algorithm was taken from https://github.com/sol-prog/N-Queens-Puzzle, which uses permutations and recursion for efficiency and was adapted to meet the challenge requirements.