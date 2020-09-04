from copy import deepcopy

class NQueens:
    """
        Generate all valid solutions for the n queens puzzle
    """
    def __init__(self, size):
        # Store the puzzle size and the number of valid solutions
        self.size = size
        self.solutions = 0
        self.solution = []

        self.solve()

    def solve(self):
        """
            Solve the n queens puzzle and save results to DB
        """
        positions = [-1] * self.size
        self.put_queen(positions, 0)

    def put_queen(self, positions, target_row):
        """
            Try to place a queen on target_row by checking all N possible cases.
            If a valid place is found the function calls itself trying to place a queen
            on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.solution.append(deepcopy(positions))
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        """
            Check if a given position is under attack from any of
            the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                return False
        return True