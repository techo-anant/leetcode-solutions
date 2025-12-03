# Question


# Solution 1 Time: O(nlog(n)), Space: aux O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head or not head.next:
            return head
    
        def makeTree(arr, l, r) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l+r + 1)//2 
            tree = TreeNode()
            tree.val = arr[mid]
            
            tree.right = makeTree(arr, mid+1, r)
            tree.left = makeTree(arr, l, mid-1)
            return tree

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        left = 0
        right = len(arr)-1 
        tree = TreeNode()
        mid = (left+right+1)//2
        tree.val = arr[mid] 
        tree.right = makeTree(arr, mid+1, right)
        tree.left = makeTree(arr, left, mid-1)

        return tree
