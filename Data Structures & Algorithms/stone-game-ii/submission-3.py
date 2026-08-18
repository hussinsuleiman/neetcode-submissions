class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf = [0] * (n+1)

        for i in range(n-1, -1, -1):
            suf[i] = suf[i+1] + piles[i]

        dp = [[0] * (n+1) for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(1, n+1):
                for k in range(1, 2*j+1):
                    if i+k-1 == n:
                        break
                    dp[i][j] = max(dp[i][j], suf[i] - dp[i+k][max(k,j)])

        return dp[0][1]