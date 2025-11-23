# Question

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Solution Time: O(n), Space: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a, b = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] == a:
                b += 1
            else:
                if b > 1:
                    b -= 1
                else:
                    a = nums[i]  

        return a
            