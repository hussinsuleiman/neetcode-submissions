class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,2**16

        while l <= r:
            mid = (l+r) // 2

            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid-1
            else:
                l = mid+1
        
        if mid - r*r < l*l - mid:
            return r
        return l