// Question

// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

 

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
 

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters if it is non-empty.

// Solution

function longestCommonPrefix(strs: string[]): string {
    
    let commonPrefix: string = "";
    let minLength: number = 200;
    let isPrefix: boolean = true;

    if(strs.length === 1) return strs[0];

    for (let str of strs) {
        if (str === "") return commonPrefix;
        if (str.length < minLength) minLength = str.length;
    }

    outerloop: for (let len = minLength; len > 0; len--){
        isPrefix = true;
        for(let i = 0; i < strs.length - 1; i++){
            if(strs[i].slice(0, len) !== strs[i+1].slice(0, len)){
                isPrefix = false;
                continue outerloop;
            }
        }
        if(isPrefix) {
            commonPrefix = strs[0].slice(0, len);
            break;
        }
    }

    return commonPrefix;

};