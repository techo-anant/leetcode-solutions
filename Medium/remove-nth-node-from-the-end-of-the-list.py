## Question 

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


## Solution 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr: Optional[ListNode] = head
        while curr != None:
            l += 1
            curr = curr.next; 

        if l == 1 and n == 1:
            return None
        
        if l == n:
            head = head.next
            return head

        curr_node: Optional[ListNode] = head
        for i in range(l-n):
            if i != l-n-1:
                curr_node = curr_node.next
                continue
            else :
                curr_node.next = (curr_node.next).next

        return head