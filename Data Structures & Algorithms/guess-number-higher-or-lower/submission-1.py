# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 0
        j = n
        m = n // 2
        g = guess(m)

        while g != 0:
            if g == 1:
                i = m+1
            else:
                j = m-1

            m = (i+j) // 2
            g = guess(m)
        
        return m
            
        