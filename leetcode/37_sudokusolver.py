'''Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:'''
from typing import List1411
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    rows[i] |= (1 << num)
                    cols[j] |= (1 << num)
                    boxes[(i // 3) * 3 + j // 3] |= (1 << num)

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        box_index = (i // 3) * 3 + j // 3
                        for num in range(9):
                            if not (rows[i] & (1 << num) or cols[j] & (1 << num) or boxes[box_index] & (1 << num)):
                                board[i][j] = str(num + 1)
                                rows[i] |= (1 << num)
                                cols[j] |= (1 << num)
                                boxes[box_index] |= (1 << num)

                                if backtrack():
                                    return True

                                board[i][j] = '.'
                                rows[i] &= ~(1 << num)
                                cols[j] &= ~(1 << num)
                                boxes[box_index] &= ~(1 << num)
                        return False
            return True

        backtrack()