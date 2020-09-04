from puzzleClass import NQueens

class TestClass:
  def test_total_solutions(self):
    """
      Test if total solutions match expected for different values of n.
      Expected solutions for n = 8, n = 9 and n = 10 were obtained from
      https://en.wikipedia.org/wiki/Eight_queens_puzzle
    """
    expected_solutions = [92, 352, 724]
    for i in range (3):
      total_solutions = NQueens(i + 8)
      assert total_solutions.solutions == expected_solutions[i]

  def test_check_place(self):
    """
      Test if check_place function returns expected value for 
      either a valid or an invalid position.
      6 first values of test_positions array were taken from 
      one of valid values found by the algorithm.
      Entire array is [0, 4, 7, 5, 2, 6, 1, 3], so next value should be 1
    """
    check_place = NQueens(8)
    test_positions = [0, 4, 7, 5, 2, 6, -1, -1]
    target_row = 6

    # Test invalid value
    column = 0
    is_valid = check_place.check_place(test_positions, target_row, column)
    assert not is_valid

    # Test valid value
    column = 1
    is_valid = check_place.check_place(test_positions, target_row, column)
    assert is_valid
