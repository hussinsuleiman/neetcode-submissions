class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        while i <= j:
            mid = (i+j) // 2
            time = 0

            for k in range(len(piles)):
                time += piles[k] // mid    
            
                if piles[k] % mid > 0:
                    time += 1

            if time > h:
                i = mid+1
            else:
                j = mid-1
        
        return i

            

            
