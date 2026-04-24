class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(queue):
            level = 1

            while queue:
                l = len(queue)

                for i in range(l):
                    x,y = queue.popleft()

                    if x > 0 and grid[x-1][y] == INF:
                        queue.append((x-1, y))
                        grid[x-1][y] = level
                    
                    if y > 0 and grid[x][y-1] == INF:
                        queue.append((x, y-1))
                        grid[x][y-1] = level
                    
                    if x < n-1 and grid[x+1][y] == INF:
                        queue.append((x+1, y))
                        grid[x+1][y] = level
                    
                    if y < m-1 and grid[x][y+1] == INF:
                        queue.append((x, y+1))
                        grid[x][y+1] = level

                level += 1

        n, m = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        bfs(queue)

