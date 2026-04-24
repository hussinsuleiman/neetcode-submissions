class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        if n == 1:
            return [[1]]

        res = [[0]*n for i in range(n)]
        res[0] = [i for i in range(1, n+1)]
        
        for i in range(1, n):
            res[i][n-1] = n+i
        
        for i in range(n-2, -1, -1):
            res[n-1][i] = 2*n + n-2-i
        
        for i in range(n-2, 0, -1):
            res[i][0] = 3*n-1 + n-2-i
        
        prev = self.generateMatrix(n-2)

        for i in range(1, n-1):
            for j in range(1, n-1):
                res[i][j] = prev[i-1][j-1] + 4*(n-1)
        
        return res