class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def order(x,y):
            res = []

            if x == m//2:
                if m%2 == 1:
                    return matrix[x][y:n-y]
                else:
                    return []

            if y == n//2:
                if n%2 == 1:
                    mat = matrix[x:m-x]
                    return [m[y] for m in mat]
                else:
                    return []

            for i in range(y,n-y):
                res.append(matrix[x][i])
            
            for i in range(x+1, m-x):
                res.append(matrix[i][n-y-1])
            
            for i in range(n-y-2, y-1, -1):
                res.append(matrix[m-x-1][i])

            for i in range(m-x-2, x, -1):
                res.append(matrix[i][y])

            return res + order(x+1,y+1)

        m,n = len(matrix), len(matrix[0])
        return order(0,0)