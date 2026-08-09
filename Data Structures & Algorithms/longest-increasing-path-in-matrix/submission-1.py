class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp = [[-1]*m for i in range(n)]

        def dfs(i,j): 
            nei = {(i+1,j), (i,j+1), (i-1,j), (i,j-1)}
            best = 0

            for x,y in nei:
                if x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] > matrix[i][j]:
                    if dp[x][y] == -1:
                        dfs(x,y)
                        
                    best = max(best, dp[x][y]) 

            dp[i][j] = 1 + best

        for i in range(n):
            for j in range(m):
                if dp[i][j] == -1:
                    dfs(i,j)
        
        rows = [max(dp[i]) for i in range(n)]
        return max(rows)