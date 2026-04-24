class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            stack = [(i,j)]
            grid[i][j] = 0
            area = 0

            while stack:
                x, y = stack.pop()
                area += 1

                if x > 0 and grid[x-1][y] == 1:
                    stack.append((x-1, y))
                    grid[x-1][y] = 0
                
                if x < n-1 and grid[x+1][y] == 1:
                    stack.append((x+1, y))
                    grid[x+1][y] = 0
                
                if y > 0 and grid[x][y-1] == 1:
                    stack.append((x, y-1))
                    grid[x][y-1] = 0
                
                if y < m-1 and grid[x][y+1] == 1:
                    stack.append((x, y+1))
                    grid[x][y+1] = 0
        
            return area
        
        n, m = len(grid), len(grid[0])
        maxArea = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea