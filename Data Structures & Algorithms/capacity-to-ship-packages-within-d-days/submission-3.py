class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def time(k):
            t = 1
            cur = 0

            for w in weights:
                if cur + w <= k:
                    cur += w
                else:
                    t += 1
                    cur = w
            
            return t
 
        l,r = max(weights), sum(weights)

        while l < r:
            mid = (l+r) // 2

            if time(mid) > days:
                l = mid+1
            else:
                r = mid
        
        return l