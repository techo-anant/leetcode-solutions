# Question
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Answer:- Time: O(n), Space: O(1)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkSymmery( n, m ) -> bool:
            if not n and not m:
                return True

            if (not n and m) or (not m and n) or (n.val != m.val):
                return False
            
            if not checkSymmery( n.left, m.right ):
                return False
            if not checkSymmery( m.left, n.right ):
                return False

            return True
        
        return checkSymmery(root.left, root.right)