class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        s = sum(stoneValue)
        dp = [-float('inf')] * (n+6)

        for i in range(n, n+6):
            dp[i] = 0

        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i], stoneValue[i] + min([dp[i+2], dp[i+3], dp[i+4]]))

            if i < n-1:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] + min([dp[i+5], dp[i+3], dp[i+4]]))
            
            if i < n-2:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] + min([dp[i+5], dp[i+6], dp[i+4]]))

        if 2*dp[0] > s:
            return 'Alice'
        elif 2*dp[0] == s:
            return 'Tie'
        return 'Bob'