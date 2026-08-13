class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    res += 4

                    for dx, dy in dirs:
                        if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and grid[x+dx][y+dy] == 1:
                            res -= 1

        return res