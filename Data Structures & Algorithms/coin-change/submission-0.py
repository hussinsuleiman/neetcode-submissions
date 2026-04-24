class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]

        for i in range(1, amount+1):
            r = float('inf')

            for c in coins:
                if i-c >= 0:
                    r = min(r, 1 + dp[i-c])

            dp.append(r)
        
        if dp[amount] == float('inf'):
            return -1

        return dp[amount]