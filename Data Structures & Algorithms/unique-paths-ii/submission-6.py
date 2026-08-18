class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        i = 0

        while i < m and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1
        
        i = 0

        while i < n and obstacleGrid[0][i] == 0:
            dp[0][i] = 1
            i += 1
            
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]: 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]