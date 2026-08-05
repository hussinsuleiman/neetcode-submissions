class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m,n = len(grid), len(grid[0])
        res = 0
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            l = len(queue)
            res += 1

            for i in range(l):
                x,y = queue.popleft()
                nei = {(x+1,y), (x,y+1), (x-1,y), (x,y-1)}

                for a,b in nei:
                    if a >= 0 and a < m and b >= 0 and b < n and grid[a][b] == 1:
                        fresh -= 1
                        grid[a][b] = 2
                        queue.append((a,b))

        return res if fresh == 0 else -1