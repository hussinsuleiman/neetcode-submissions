class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(n):
            t = 0

            for p in piles:
                t += (p+n-1)//n
            
            return t

        i,j = 1, max(piles)

        while i < j:
            mid = (i+j) // 2

            if time(mid) > h:
                i = mid+1
            else:
                j = mid
        
        return i