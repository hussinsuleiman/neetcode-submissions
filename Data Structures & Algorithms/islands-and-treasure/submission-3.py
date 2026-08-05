class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        m,n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            x,y = queue.popleft()
            nei = {(x-1,y), (x+1,y), (x,y+1), (x,y-1)}
            
            for a,b in nei:
                if a >= 0 and a < m and b >= 0 and b < n and grid[a][b] == 2147483647:
                    grid[a][b] = grid[x][y] + 1
                    queue.append((a,b))