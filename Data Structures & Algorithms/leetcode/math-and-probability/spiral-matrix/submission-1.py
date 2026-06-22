class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m,n = len(matrix), len(matrix[0])

        if m == 1:
            return matrix[0]
        
        if n == 1:
            col = [matrix[i][0] for i in range(m)]
            return col
        
        res = [matrix[0][j] for j in range(n)]
        print(m,n,res)
        
        for i in range(1, m):
            res.append(matrix[i][n-1])
        
        for j in range(n-2, -1, -1):
            res.append(matrix[m-1][j])
        
        for i in range(m-2, 0, -1):
            res.append(matrix[i][0])
        
        new = []

        for i in range(1, m-1):
            row = []

            for j in range(1, n-1):
                row.append(matrix[i][j])
            
            new.append(row)

        res += self.spiralOrder(new)
        return res