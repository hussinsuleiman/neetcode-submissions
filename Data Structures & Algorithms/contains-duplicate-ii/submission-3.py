class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        elts = set()
        n = len(nums)

        for i in range(k+1):
            if i == n:
                return False

            if nums[i] in elts:
                return True
            elts.add(nums[i])

        l,r = 0,k+1

        while r < n:
            elts.remove(nums[l])
            l += 1

            if nums[r] in elts:
                return True
            
            elts.add(nums[r])
            r += 1
        
        return False