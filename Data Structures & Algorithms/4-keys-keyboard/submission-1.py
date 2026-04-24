class Solution:
    def maxA(self, n: int) -> int:
        dp = [1,2,3]

        for i in range(3, n):
            m = dp[i-1] + 1

            for j in range(i-2):
                m = max(m, dp[j] * (i-1-j))
            
            dp.append(m)
        
        return dp[n-1]