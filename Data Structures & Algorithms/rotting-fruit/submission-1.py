class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(queue, nbFresh):
            level = 0

            while queue and nbFresh > 0:
                l = len(queue)

                for i in range(l):
                    x,y = queue.popleft()

                    if x > 0 and grid[x-1][y] == 1:
                        queue.append((x-1, y))
                        grid[x-1][y] = 2
                        nbFresh -= 1
                    
                    if y > 0 and grid[x][y-1] == 1:
                        queue.append((x, y-1))
                        grid[x][y-1] = 2
                        nbFresh -= 1
                    
                    if x < n-1 and grid[x+1][y] == 1:
                        queue.append((x+1, y))
                        grid[x+1][y] = 2
                        nbFresh -= 1
                    
                    if y < m-1 and grid[x][y+1] == 1:
                        queue.append((x, y+1))
                        grid[x][y+1] = 2
                        nbFresh -= 1

                level += 1
            
            if nbFresh > 0:
                return -1
            
            return level

        n, m = len(grid), len(grid[0])
        queue = deque()
        nbFresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    nbFresh += 1
        
        return bfs(queue, nbFresh)
