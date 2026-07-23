class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        exp = 1

        for i in range(1, n+1):
            dp[i] = 1 + dp[i-exp]

            if (i+1) >= exp*2:
                exp *= 2
        
        return dp