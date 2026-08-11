class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp = [[0]*(ls+1) for i in range(lt+1)]

        for i in range(ls+1):
            dp[0][i] = 1
        
        for i in range(1, lt+1):
            for j in range(1, ls+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]