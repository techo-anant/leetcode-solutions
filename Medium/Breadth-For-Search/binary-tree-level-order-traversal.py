# Question

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Answer:- Time: O(n), Space: O(n)

from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = defaultdict(list)
        q = deque([(0, root)])

        while q:
            level, node = q.popleft()
            res[level].append(node.val)
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
        
        ans = []
        h = len(res.keys())
        if res:
            for i in range(h):
                ans.append(res[i])

        return ans
    
# Better space alternative and deleting redundancy

class Solution2:
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            len_level = len(q)
            level = []

            for _ in range(len_level):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res