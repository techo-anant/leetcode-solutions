# Question 

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Answer:- Time: O(m * n * 4l); l-> word length, Space: O(l)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def findWord( r, c, charat):
            if charat == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[charat]:
                return False
            
            board[r][c] = "."
            
            for d in direction:
                if findWord( r-d[0], c-d[1], charat+1):
                    return True
            
            board[r][c] = word[charat]
            return False



        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if findWord( r, c, 0):
                        return True
        
        return False
    
#  Additionally we can prune more, like using counter first to validate if the chars exist and maybe reverse the word if word[0] occurs more than word[-1]