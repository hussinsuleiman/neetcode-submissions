class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        seen = set()

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in seen or grid[i][j] == 0:
                return 0

            seen.add((i,j))
            a,b,c,d = dfs(i+1,j), dfs(i-1,j), dfs(i,j+1), dfs(i,j-1)
            return 1 + a + b + c + d

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))

        return res