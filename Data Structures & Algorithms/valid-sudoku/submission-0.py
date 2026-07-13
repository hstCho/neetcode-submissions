class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(9)}
        column = {i: set() for i in range(9)}
        square = {(i, j): set() for i in range(3) for j in range(3)}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                digit = board[i][j]
                if digit == ".":
                    continue
                if (digit in row[i] 
                    or digit in column[j] 
                    or digit in square[(i//3, j//3)]
                    ):
                    return False
                else:
                    row[i].add(digit)
                    column[j].add(digit)
                    square[(i//3, j//3)].add(digit)
        return True
                