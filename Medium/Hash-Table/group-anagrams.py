# Question 

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Answer Time: O(n*k), Space: O(n*k)

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def hashedCounter( string ):
            letters = [0]*26
            for s in string:
                letters[ord(s) - ord('a')] += 1
        
            # hashed = ""
            # for i in range(0, 26):
            #     if letters[i] != 0:
            #         hashed += (chr(ord('a') + i) + str(letters[i]))
            return tuple(letters)

        a = defaultdict(list)

        for string in strs:
            hashed = hashedCounter(string)
            a[hashed].append(string)
            
        return list(a.values())

# Answer Time: O(n*klog(k)), Space: O(k)

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    a = defaultdict(list)
    for string in strs:
        sorted_key = ''.join(sorted(string))
        a[sorted_key].append(string)
    return list(a.values())


            
