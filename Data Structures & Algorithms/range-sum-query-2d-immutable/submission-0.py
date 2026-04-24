class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        
        for i in range(len(matrix)):
            sumsRow = [0]

            for j in range(len(matrix[0])):
                sumsRow.append(sumsRow[-1] + matrix[i][j])

            self.sums.append(sumsRow)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for row in range(row1, row2 + 1):
            total += self.sums[row][col2+1] - self.sums[row][col1]
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)