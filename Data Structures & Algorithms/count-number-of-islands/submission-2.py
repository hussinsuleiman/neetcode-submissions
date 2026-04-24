class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            stack = [(i,j)]
            grid[i][j] = '0'

            while stack:
                x, y = stack.pop()

                if x > 0 and grid[x-1][y] == '1':
                    stack.append((x-1, y))
                    grid[x-1][y] = '0'
                
                if x < n-1 and grid[x+1][y] == '1':
                    stack.append((x+1, y))
                    grid[x+1][y] = '0'
                
                if y > 0 and grid[x][y-1] == '1':
                    stack.append((x, y-1))
                    grid[x][y-1] = '0'
                
                if y < m-1 and grid[x][y+1] == '1':
                    stack.append((x, y+1))
                    grid[x][y+1] = '0'

        n, m = len(grid), len(grid[0]) 
        nbIslands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j)
                    nbIslands += 1
        
        return nbIslands
            
