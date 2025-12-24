# Question

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Answer:- Time: O(m*n), Space: O(1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def markIsland( r, c ):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'

            for d in directions:
                markIsland( r-d[0], c-d[1])
            
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    res += 1
                    markIsland(r , c)
                
        return res
            