class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i,j = 1, 2**16

        while i <= j:
            m = (i+j) // 2

            if m*m == num:
                return True
            elif m*m > num:
                j = m-1
            else:
                i = m+1
        
        return False