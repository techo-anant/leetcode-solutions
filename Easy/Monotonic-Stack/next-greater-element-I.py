# Question
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

# Constraints:

# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
 





# Solution Time: O(n^2), Space: O(n) - Using Hash Table only

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = dict((x, i) for i, x in enumerate(nums2))

        ans = [-1]*len(nums1)

        for i in range(0, len(nums1)):
            if a[nums1[i]] == len(nums2) -1 :
                continue
            for j in range(a[nums1[i]]+1, len(nums2)):
                if nums1[i] < nums2[j]:
                    ans[i] = nums2[j]
                    break        
        
        return ans
        

# Follow up: Could you find an O(nums1.length + nums2.length) solution?

# Solution Time: O(n+m), Space: O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashed = {}

        for num in nums2:
            if stack:
                while (stack and num > stack[-1]):
                    hashed[stack.pop()] = num
            stack.append(num)
        
        while stack:
            hashed[stack.pop()] = -1
    
        ans = []

        for num in nums1:
            ans.append(hashed[num])
        
        return ans


        
