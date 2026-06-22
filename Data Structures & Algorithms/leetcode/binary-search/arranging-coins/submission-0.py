class Solution:
    def arrangeCoins(self, n: int) -> int:
        i,j = 1, 2**16

        while i <= j:
            m = (i+j) // 2

            if m*(m+1) > 2*n:
                j = m-1
            else:
                i = m+1
        
        if i*(i+1) > 2*n:
            return i-1
        
        return i