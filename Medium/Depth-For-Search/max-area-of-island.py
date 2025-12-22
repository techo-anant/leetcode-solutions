# Question

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

# Answer:- Time: O(m*n), Space: O(n*m)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len( grid[0] )  
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs( r, c ):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            curr = 1

            for d in direction:
                curr += dfs( r + d[0], c + d[1])

            return curr

        maxx = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxx = max(maxx, area)

        return maxx