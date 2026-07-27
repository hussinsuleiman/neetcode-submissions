class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        def dfs(i, j, seen):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or (i,j) in seen:
                return
            
            seen.add((i,j))
            dfs(i+1, j, seen)
            dfs(i, j+1, seen)
            dfs(i-1, j, seen)
            dfs(i, j-1, seen)

        nbIslands = 0
        seen = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in seen:
                    dfs(i, j, seen)
                    nbIslands += 1
        
        return nbIslands