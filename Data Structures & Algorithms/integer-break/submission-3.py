class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n-1

        dp = [1]

        for i in range(1, n+1):
            best = 1

            for j in range(1, i+1):
                best = max(best, j * dp[i-j])
            
            dp.append(best)

        return dp[-1]