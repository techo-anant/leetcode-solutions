# Question

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.


# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


# Solution [O(n)] n is the length of list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        l = 0
        curr = head
        last = None
        curr_last = None
        
        while curr:
            l += 1
            last = curr
            curr = curr.next
        
        curr_last = last

        curr = head
        prev = curr
        for i in range(l):
            if not curr:
                break
            if i == l-1 and last == curr_last:
                break 
            if curr.val >= x:
                shift = curr
                if curr == head:
                    curr = curr.next
                    head = shift.next
                    prev = shift.next
                    curr_last.next = shift 
                    shift.next = None
                    curr_last = curr_last.next
                else: 
                    curr = curr.next  
                    prev.next = curr
                    curr_last.next = shift
                    shift.next = None
                    curr_last = curr_last.next
            else:
                prev = curr
                curr = curr.next

        return head



        