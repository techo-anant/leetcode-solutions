// Question 
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21


// Constraints:

// -231 <= x <= 231 - 1


// Solution 
function reverse(x: number): number {
    if (x === 0) return 0;
    let y: number = x;

    if (x < 0) {
        y = -1 * y;
    }
    let num: string = String(y);
    let revNum: string = num.split("").reverse().join("");
    y = Number(revNum);
    if (x < 0) {
        y = -1 * y;
    }
    if (y <= -2147483648 || y >= 2147483647) return 0;
    return y;
};