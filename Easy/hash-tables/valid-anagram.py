# Question

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Solution Time: O(n), Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0]*26

        for i in s:
            count[ord(i) - ord('a')] += 1
        

        for i in t:
            if count[ord(i) - ord('a')] == 0:
                return False
            count[ord(i) - ord('a')] -= 1
        
        return True
            
            

# For
# What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a = dict()

        for i in s:
            if a.get(i):
                a[i] += 1
            else:
                a[i] = 1
            
        for j in t:
            if a.get(j):
                if a.get(j) > 1:
                    a[j] -= 1
                else:
                    a.pop(j)
            else:
                return False
        
        return True