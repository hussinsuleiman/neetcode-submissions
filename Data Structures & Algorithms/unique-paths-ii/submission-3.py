class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for i in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for k in range(i, n):
                    dp[0][k] = 0
                break

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for k in range(i, m):
                    dp[k][0] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                cur = 0

                if obstacleGrid[i-1][j] == 0:
                    cur += dp[i-1][j]
                
                if obstacleGrid[i][j-1] == 0:
                    cur += dp[i][j-1]

                dp[i][j] = cur

        return dp[-1][-1]