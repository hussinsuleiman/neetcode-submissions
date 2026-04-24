class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp = [[0]*m for i in range(n)]

        for i in range(m):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        
        for i in range(n):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    done = False
        
                    for k in range(dp[i-1][j-1]):
                        if matrix[i][j-1-k] == '0' or matrix[i-1-k][j] == '0':
                            dp[i][j] += k
                            done = True
                            break
                    
                    if not done:
                        dp[i][j] += dp[i-1][j-1]                   
        
        m = max(dp[0])

        for i in range(1,n):
            m = max(m, max(dp[i]))

        return m ** 2