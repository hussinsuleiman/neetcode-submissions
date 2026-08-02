class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        i,j = 0, m*n-1

        while i <= j:
            mid = (i+j) // 2
            r,c = mid//n, mid%n

            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] < target:
                i = mid+1
            else:
                j = mid-1

        return False       