class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n//2):
            for j in range(n//2):
                a,b,c,d = matrix[j][i], matrix[i][n-1-j], matrix[n-1-j][n-1-i], matrix[n-1-i][j]
                matrix[j][i], matrix[i][n-1-j], matrix[n-1-j][n-1-i], matrix[n-1-i][j] = d,a,b,c
        
        if n%2 == 1:
            for i in range(n//2):
                a,b,c,d = matrix[n//2][i], matrix[i][n//2], matrix[n-1-n//2][n-1-i], matrix[n-1-i][n//2]
                matrix[n//2][i], matrix[i][n//2], matrix[n-1-n//2][n-1-i], matrix[n-1-i][n//2] = d,a,b,c