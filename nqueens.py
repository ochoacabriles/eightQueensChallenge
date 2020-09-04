import os
from datetime import datetime
from db.controller import storeSolutions
from puzzleClass import NQueens

def main():
    startTime = datetime.now()
    n = 8
    solutions = {}
    while n <= 9:
        puzzleSolution = NQueens(n)
        solutions[n] = puzzleSolution.solution
        n += 1
    for key in solutions:
        print(key)
        storeSolutions(solutions[key], key)
    endTime = datetime.now() - startTime
    print('Tiempo requerido: ', endTime.total_seconds(), 's')

if __name__ == '__main__':
    # execute only if run as a script
    main()
