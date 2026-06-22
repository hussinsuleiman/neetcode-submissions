class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[(0,0)]*(n+1) for i in range(n+1)]
        pre = [0]

        for p in piles:
            pre.append(pre[-1]+p)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if 2*j >= i:
                    dp[i][j] = (pre[-1]-pre[-1-i], 0)
                    continue

                M = 0
                m = 10000000

                for l in range(1, 2*j+1):
                    M = max(M, dp[i-l][max(l,j)][1] + pre[-1-i+l]-pre[-1-i])
                    m = min(m, dp[i-l][max(l,j)][0])
                
                dp[i][j] = (M,m)

        return dp[-1][1][0]