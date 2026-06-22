class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts)
        s = min(n-k+1, maxPts)

        for i in range(k, min(n+1, k + maxPts)):
            dp[i] = 1

        for i in range(k-1, -1, -1):
            dp[i] = float(s) / maxPts
            s = s + dp[i] - dp[i + maxPts]

        return dp[0]