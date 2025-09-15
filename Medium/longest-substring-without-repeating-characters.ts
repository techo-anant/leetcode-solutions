// Question

// Given a string s, find the length of the longest substring without duplicate characters.



// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


// Constraints:

// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.

// Solution

function lengthOfLongestSubstring(s: string): number {
    if (!s) return 0;
    let str: string[] = s.split("");
    let maxLen: number = 0;
    let currLen: number = 0;
    let charFound: string[] = [];
    for (let i = 0; i < str.length; i++) {
        if (!charFound.includes(str[i])) {
            currLen += 1;
            charFound.push(str[i]);
        } else {
            let idx = charFound.indexOf(str[i]);
            charFound = charFound.slice(idx + 1);
            charFound.push(str[i]);
            currLen = charFound.length;
        }
        if (currLen > maxLen) maxLen = currLen;
    }
    return maxLen;
};