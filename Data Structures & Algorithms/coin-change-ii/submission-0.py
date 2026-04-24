class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        l = len(coins)
        dp = [[1]*(l+1) for i in range(amount+1)]

        for i in range(1, amount+1):
            dp[i][0] = 0

            for j in range(1, l+1):
                dp[i][j] = dp[i][j-1]

                if coins[j-1] <= i:
                    dp[i][j] += dp[i-coins[j-1]][j]
        
        return dp[-1][-1]