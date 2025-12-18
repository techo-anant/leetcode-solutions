# Question

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Answer:- Time: O(n), Space: O(1)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if (not p and q) or (not q and p ) or p.val != q.val:
                return False

            if not dfs(p.left , q.left):
                return False

            if not dfs(p.right, q.right):
                return False
            
            return True
        
        return dfs(p, q)