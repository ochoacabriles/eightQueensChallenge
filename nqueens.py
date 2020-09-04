import os
from datetime import datetime
from db.controller import storeSolutions
from puzzleClass import NQueens

if __name__ == '__main__':
    """
        Iterate over n to find valid solutions.
        In local tests, 13 is the highest n which can be calculated
        within 10 minutes on a laptop
    """
    startTime = datetime.now()
    n = 8
    solutions = {}
    while n <= 13:
        puzzleSolution = NQueens(n)
        solutions[n] = puzzleSolution.solution
        n += 1
    for key in solutions:
        storeSolutions(solutions[key], key)
    endTime = datetime.now() - startTime
    print('Tiempo requerido: ', endTime.total_seconds(), 's')