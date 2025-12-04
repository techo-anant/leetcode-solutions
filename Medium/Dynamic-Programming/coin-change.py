# Question

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# Solution Time: O(amount^n), Space: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # ttl exceeded - Worst soln

        def dfs( amt ):
            
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')

            min_coins = float('inf')

            for coin in coins:
                result = dfs(amt - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
                
            return min_coins
        
        ans = dfs( amount )

        return ans if ans != float('inf') else -1
    
# Solution Time: O(amount * n), Space: O(amount) - memo

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # trying memoization - getting better

        memo = {}

        def dfs( amt ):
            if amt == 0:
                return 0
            if amt < 0:
                return float('Inf')

            if amt in memo:
                return memo[amt]
            
            min_coins = float('inf')
            for coin in coins:
                result = dfs(amt - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
            
            memo[amt] = min_coins
            return min_coins
        
        ans = dfs( amount )
        return ans if ans != float('inf') else -1
    
# Solution Time: O(amount * n), Space: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # trying bottom up - best

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1