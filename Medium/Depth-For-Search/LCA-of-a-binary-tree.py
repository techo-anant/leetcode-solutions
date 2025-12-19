# Question

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Answer:- Time: O(n), Space: O(1)

# works but trickier

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0]) 
        dp = [[False]*n for _ in range(m)]

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
        def markIsland( r, c ):

            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0' or dp[r][c]:
                return 
            
            dp[r][c] = True

            for d in directions:
                markIsland( r-d[0], c-d[1])
            
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not dp[r][c]:
                    res += 1
                    markIsland(r , c)
                
        return res
    
# much cleaner

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor( root.left, p, q)
        right = self.lowestCommonAncestor( root.right, p, q)

        if left and right:
            return root
        
        return left or right