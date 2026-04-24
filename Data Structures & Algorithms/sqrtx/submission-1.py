class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x

        while i < j:
            m = (i+j) // 2

            if m*m < x:
                i = m+1
            elif m*m > x:
                j = m-1
            else:
                return m
        
        if i*i > x:
            return i-1
        else:
            return i