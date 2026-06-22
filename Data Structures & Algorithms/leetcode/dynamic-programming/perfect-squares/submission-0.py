class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]

        for i in range(1, n+1):
            cur = float('inf')
            j = 1

            while j**2 <= i:
                cur = min(cur, 1 + dp[i - j**2])
                j += 1
            
            dp.append(cur)
        
        return dp[-1]