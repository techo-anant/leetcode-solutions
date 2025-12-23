# Question

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Answer:- Time: O(h+k), Space: O(h)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.remaining = k
        self.answer = None

        def inorder( node ):
            if not node:
                return 

            if node.left:
                inorder( node.left )
                if self.answer:
                    return
            
            self.remaining -= 1
            if self.remaining == 0:
                self.answer = node.val

            if node.right:
                inorder( node.right )
                if self.answer:
                    return  
            return
        
        inorder( root )
        return self.answer