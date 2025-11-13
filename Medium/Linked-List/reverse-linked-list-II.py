# Question

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right :
            return head

        def reverse(node: Optional[ListNode], n) -> (Optional[ListNode], Optional[ListNode] , Optional[ListNode]):
            if n == 1:
                return node, node, node.next
            
            l, r, n = reverse(node.next, n-1)
            r.next = node
            
            return (l, r.next, n)


        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        curr = head
        if left == 1:
                l, r, n = reverse(head, right)
                head = l
                r.next = n
        else:
            for i in range(1, l+1):
                if i == left-1:
                    l, r, n = reverse(curr.next, right - i)
                    curr.next = l
                    r.next = n
                    break
                curr = curr.next

        return head

                
                

