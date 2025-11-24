# Question

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

# Answer Time: O(n), Space: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_list = list(s)
        t_list = list(t)
        l = len(s)

        d = dict({t_list[0]:s_list[0]})

        t_list[0] = s_list[0]

        for i in range(1, l):
            if d.get(t_list[i]):
                t_list[i] = d.get(t_list[i])
                if t_list[i] != s_list[i]:
                    return False
            else:
                if s_list[i] in d.values():
                    return False
                else:
                    d[t_list[i]] = s_list[i]
                    t_list[i] = s_list[i]
        
        return s_list == t_list