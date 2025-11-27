# Question

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
 

# Follow-up: Can you implement the stack using only one queue?

# Solution

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.use = False

    def push(self, x: int) -> None:
        if not self.use:
            self.q2.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        if not self.use:
            if len(self.q2) == 0:
                return None
            
            while len(self.q2) != 1:
                self.q1.append(self.q2.popleft())
            
            self.use = True

            return self.q2.popleft()
        else:
            if len(self.q1) == 0:
                return None
            
            while len(self.q1) != 1:
                self.q2.append(self.q1.popleft())

            self.use = False

            return self.q1.popleft()

    def top(self) -> int:
        if not self.use:
            if len(self.q2) == 0:
                return None
            
            while len(self.q2) != 1:
                self.q1.append(self.q2.popleft())
            
            top = self.q2.popleft()
            self.q1.append(top)
            
            self.use = True

            return top
        else:
            if len(self.q1) == 0:
                return None
            
            while len(self.q1) != 1:
                self.q2.append(self.q1.popleft())
            
            top = self.q1.popleft()
            self.q2.append(top)

            self.use = False

            return top

    def empty(self) -> bool:
        if not self.use:
            return len(self.q2) == 0
        else:
            return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.popleft()
# param_3 = obj.top()
# param_4 = obj.empty()