class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(1, numRows):
            new = [1] * (i+1)
            prev = output[-1]

            for j in range(1, i):
                new[j] = prev[j-1] + prev[j]
            
            output.append(new)
        
        return output