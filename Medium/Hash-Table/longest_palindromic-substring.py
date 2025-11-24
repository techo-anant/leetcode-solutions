## Question 
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.



## Solution O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def in_bounds(i , j, s):
            return 0 < i and j < (len(s));

        longest = ""

        s = "#" + "#".join(char for char in s) + "#"
        for i in range(1, len(s) - 1):
            curr = s[i];
            k = 1
            while in_bounds(i - k, i + k, s) and s[i-k] == s[i+k]:
                curr = s[i-k] + curr + s[i+k]
                k += 1
            longest = curr.replace("#", "") if len(curr)<len(s) and len(curr.replace("#", "")) > len(longest) else longest
        
        return longest

## Solution O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def expand_around_center(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start , max_len = 0, 0
        for i in range(len(s)):
            start_from_same_char = expand_around_center(i, i)

            start_from_adjacent_char = expand_around_center(i, i+1)

            curr_len = max(start_from_same_char, start_from_adjacent_char)

            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2
        
        return s[start:start + max_len]
