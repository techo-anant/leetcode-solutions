// Question

// Given a triangle array, return the minimum path sum from top to bottom.

// For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



// Example 1:

// Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
// Output: 11
// Explanation: The triangle looks like:
//    2
//   3 4
//  6 5 7
// 4 1 8 3
// The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
// Example 2:

// Input: triangle = [[-10]]
// Output: -10


// Constraints:

// 1 <= triangle.length <= 200
// triangle[0].length == 1
// triangle[i].length == triangle[i - 1].length + 1
// -104 <= triangle[i][j] <= 104

// Solution

function minimumTotal(triangle: number[][]): number {
    let dp: number[][] = triangle.map(row => Array(row.length).fill(Infinity));

    dp[0][0] = triangle[0][0]
    let len: number = triangle.length;

    for (let i = 1; i < len; i++) {
        for (let j = 0; j < i + 1; j++) {
            if (j === 0) dp[i][j] = dp[i - 1][0] + triangle[i][j];
            else if (j === i) dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
            else dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j];
        }
    }
    return Math.min(...dp[dp.length - 1]);

};