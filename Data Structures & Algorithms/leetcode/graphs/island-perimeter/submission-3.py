class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        have1 = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += 4
                    have1.add((i,j))

        for (i,j) in have1:
            if (i-1, j) in have1:
                total -= 1
            
            if (i+1, j) in have1:
                total -= 1
            
            if (i, j-1) in have1:
                total -= 1
            
            if (i, j+1) in have1:
                total -= 1
        
        return total