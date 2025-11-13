## Question 

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


## Solution 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = 0
        curr = head
        last = curr
        while curr:
            last = curr
            l += 1
            curr = curr.next
        
        k = k % l

        if k == 0 or k == l:
            return head

        rotate = head
        prev_head = head
        for i in range(l - k):
            if i == l-k-1:
                head = rotate.next
                rotate.next = None
                last.next = prev_head
                break
            rotate = rotate.next
        
        return head
