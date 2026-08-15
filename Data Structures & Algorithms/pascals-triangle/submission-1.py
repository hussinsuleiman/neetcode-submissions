class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows-1):
            new = [1] * (i+2)

            for j in range(1, i+1):
                new[j] = res[-1][j-1] + res[-1][j]

            res.append(new)
        
        return res