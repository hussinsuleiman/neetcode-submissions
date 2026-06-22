class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal(s, a, b):
            while a < b:
                if s[a] != s[b]:
                    return False
                
                a += 1
                b -= 1
            
            return True
        
        dp = [1]
        l = len(s)

        for i in range(1, l):
            res = dp[i-1]

            for j in range(i, -1, -1):
                if isPal(s, j, i):
                    res += 1

            dp.append(res)

        return dp[l-1]        