class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*(l+2) for i in range(2)]

        for i in range(l-1, -1, -1):
            dp[0][i] = max(dp[1][i+1] - prices[i], dp[0][i+1])
            dp[1][i] = max(dp[0][i+2] + prices[i], dp[1][i+1])

        return dp[0][0]