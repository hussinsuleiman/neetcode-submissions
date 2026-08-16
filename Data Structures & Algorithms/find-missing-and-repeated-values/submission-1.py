class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [0, 0]

        for i in range(n):
            for j in range(n):
                row, col = (abs(grid[i][j])-1)//n, (abs(grid[i][j])-1)%n

                if grid[row][col] < 0:
                    res[0] = abs(grid[i][j])
                else:
                    grid[row][col] *= -1
        
        for i in range(n):
            done = False

            for j in range(n):
                if grid[i][j] > 0:
                    res[1] = n*i+j+1
                    done = True
                    break

            if done:
                break

        return res