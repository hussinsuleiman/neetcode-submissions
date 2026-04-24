class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[(0,0)]*l for i in range(l)]

        for i in range(l):
            dp[i][i] = (1-piles[i], 1+piles[i])     

        for i in range(1, l):
            for j in range(l-i):
                dp[j][j+i] = (min(dp[j][j+i-1][1] - piles[i+j], dp[j+1][j+i][1] - piles[j]) , max(dp[j][j+i-1][0] - piles[i+j], dp[j+1][j+i][0] - piles[j]))
        
        return dp[0][l-1][0] <= 0