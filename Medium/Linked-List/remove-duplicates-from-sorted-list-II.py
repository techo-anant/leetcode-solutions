# Question 

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.




## Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        head = None
        while curr:
            removal = False
            while curr.next and curr.val == curr.next.val:
                if prev:
                    prev.next = curr.next
                curr = curr.next
                removal = True
                continue
            
            if removal:
                if prev:
                    prev.next = curr.next
                curr = curr.next
                continue
            else:
                if not prev:
                    head = curr
                    prev = curr
                else:
                    prev.next = curr
                    prev = prev.next
            curr = curr.next

        return head
