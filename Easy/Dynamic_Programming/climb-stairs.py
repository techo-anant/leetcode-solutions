# Question

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# Solution Time: O(n), Space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        prev_1 = 2
        prev_2 = 1

        if n == 1:
            return prev_2
        elif n == 2:
            return prev_1

        ways = 0
        for _ in range(n-2):  # as we have 2 results as base case
            ways = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = ways
        
        return ways
    
