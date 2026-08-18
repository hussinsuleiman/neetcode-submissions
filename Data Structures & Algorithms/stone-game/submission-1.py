class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        s = sum(piles)
        n = len(piles)
        dp = [[0] * (n+1) for i in range(n+1)]
        
        for i in range(n):
            dp[i][i+1] = piles[i]
        
        for k in range(2, n+1):
            for i in range(n+1-k):
                j = i+k
                dp[i][j] = max(piles[i] + min(dp[i+1][j-1], dp[i+2][j]), piles[j-1] + min(dp[i+1][j-1], dp[i][j-2]))
        
        return dp[0][n] > s//2