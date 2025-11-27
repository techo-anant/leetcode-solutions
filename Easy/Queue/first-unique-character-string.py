# Question

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# Solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0

        counter = [0]*26

        for st in s:
            counter[ord(st) - ord('a')] += 1
        
        for i in range(len(s)):
            if counter[ord(s[i]) - ord('a')] == 1:
                return i

        return -1