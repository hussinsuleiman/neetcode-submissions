class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        if l1+l2 != l3:
            return False
        
        dp = [[False]*(l1+1) for i in range(l2+1)]
        dp[0][0] = True

        for i in range(1, l1+1):
            dp[0][i] = (s1[-i:] == s3[-i:])

        for i in range(1, l2+1):
            dp[i][0] = (s2[-i:] == s3[-i:])

        for i in range(1, l2+1):
            for j in range(1, l1+1):
                val = False

                if s2[-i] == s3[-i-j] and dp[i-1][j]:
                    val = True
                
                elif s1[-j] == s3[-i-j] and dp[i][j-1]:
                    val = True
                
                dp[i][j] = val
        
        return dp[-1][-1]