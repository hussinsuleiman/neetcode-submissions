class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m,k,n = len(mat1), len(mat1[0]), len(mat2[0])
        out = []

        for i in range(m):
            new = []

            for j in range(n):
                p = 0

                for l in range(k):
                    p += mat1[i][l] * mat2[l][j]
                
                new.append(p)
            
            out.append(new)
        
        return out