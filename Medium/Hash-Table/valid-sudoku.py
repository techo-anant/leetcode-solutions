# Question

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


# Answer

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(27):
            seen = {
                "1":False, 
                "2":False, 
                "3":False, 
                "4":False, 
                "5":False, 
                "6":False, 
                "7":False, 
                "8":False, 
                "9":False
            }
            if i//9 == 0:
                for char in board[i]:
                    if char.isdigit():
                        if seen[char] == False:
                            seen[char] = True
                        else:
                            return False
            elif i//9 == 1:
                for j in range(9):
                    if board[j][i%9].isdigit():
                        if seen[board[j][i%9]] == False:
                            seen[board[j][i%9]] = True
                        else:
                            return False
            else:
                box = i - 18
                row_start = 3 * (box // 3)
                col_start = 3 * (box % 3)
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        char = board[r][c]
                        if char.isdigit():
                            if seen[char]:
                                return False
                            seen[char] = True

        return True