class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns,np = len(s), len(p)
        dp = [[False]*(ns+1) for i in range(np+1)]
        dp[0][0] = True
        i = 1
        
        while i < np and p[i] == '*':
            dp[i+1][0] = True
            i += 2

        for i in range(1, np+1):
            for j in range(1, ns+1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[i-1] == '*':
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        dp[i][j] = dp[i][j-1] or dp[i-2][j-1] 
                    
                    dp[i][j] = dp[i][j] or dp[i-2][j]
        
        return dp[np][ns]