# Question 

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Answer:- Time: O(n*m), Space: O(1)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkTrees ( main, sub ):
            if not main and not sub:
                return True
            
            if (not main and sub) or (main and not sub) or ( main.val != sub.val):
                return False

            if not checkTrees( main.left, sub.left ) or not checkTrees( main.right, sub.right):
                return False

            return True


        def findRoot ( main, val ):
            if not main:
                return False

            if main.val == val:
                if checkTrees( main, subRoot):
                    return True
            
            if findRoot( main.left , val ) or findRoot( main.right , val ):
                return True
            
            return False
        
        return findRoot( root, subRoot.val)
            