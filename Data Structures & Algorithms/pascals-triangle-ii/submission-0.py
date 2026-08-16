class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            new = [1] * (i+2)

            for j in range(1, i+1):
                new[j] = row[j-1] + row[j]

            row = new

        return row