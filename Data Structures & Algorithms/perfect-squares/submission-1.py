class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        root = 1

        for i in range(1,n+1):
            if i >= (root+1) * (root+1):
                root += 1

            best = float('inf')

            for j in range(1, root+1):
                best = min(best, dp[i - j**2] + 1)
            
            dp.append(best)

        return dp[-1]