class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1, 2]

        for i in range(3, n):
            r = i

            for j in range(i-1, 0, -1):
                r = max(r, (i-j) * dp[j])
            
            dp.append(r)
        
        res = 0

        for j in range(n-1, 0, -1):
            res = max(res, (n-j) * dp[j])

        return res