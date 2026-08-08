class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        l = len(coins)
        dp = [[0]*(l+1) for i in range(amount+1)]
        
        for j in range(l+1):
            dp[0][j] = 1

        for i in range(1, amount+1):
            for j in range(1, l+1):
                if coins[j-1] > i:
                    dp[i][j] = dp[i][j-1]

                dp[i][j] = dp[i-coins[j-1]][j] + dp[i][j-1]
        
        return dp[-1][-1]