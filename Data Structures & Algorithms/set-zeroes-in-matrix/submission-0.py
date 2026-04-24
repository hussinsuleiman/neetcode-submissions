class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
            
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0
        
        for c in cols:
            for i in range(m):
                matrix[i][c] = 0