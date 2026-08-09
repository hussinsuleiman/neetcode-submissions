class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        if l1 + l2 != l3:
            return False

        dp = [[False]*(l2+1) for i in range(l1+1)]
        dp[0][0] = True
        j = l2-1

        while j >= 0 and s2[j] == s3[l1+j]:
            dp[0][l2-j] = True
            j -= 1
        
        i = l1-1

        while i >= 0 and s1[i] == s3[l2+i]:
            dp[l1-i][0] = True
            i -= 1

        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if s1[i] == s3[i+j] and dp[l1-i-1][l2-j]:
                    dp[l1-i][l2-j] = True
                
                elif s2[j] == s3[i+j] and dp[l1-i][l2-j-1]:
                    dp[l1-i][l2-j] = True
        
        return dp[l1][l2]