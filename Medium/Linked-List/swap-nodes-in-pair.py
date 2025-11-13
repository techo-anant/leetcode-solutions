## Question 

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:
# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

## Solution 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head
        
        curr = head
        i = 1
        while curr:
            if not curr.next:
                return head
            
            if i == 1:
                head = head.next
                i += 1
            
                to_switch = curr.next
                if (curr.next).next == None:
                    curr.next = None
                else:
                    curr.next = (curr.next).next 
                to_switch.next = curr
            else:
                if not (curr.next).next:
                    return head
                else:  
                    to_switch = curr.next
                    curr.next = (curr.next).next
                    to_switch.next = (curr.next).next
                    (curr.next).next = to_switch
                    curr = to_switch
        return head
                