class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l,r = 0,1
        s = sum(nums)
        cur = nums[0]
        best = nums[0]
        n = len(nums)

        while r < n:
            if cur < 0:
                l = r
                cur = nums[r]
            else:
                cur += nums[r]
            
            best = max(best, cur)
            r += 1
        
        cur = nums[0]
        worst = nums[0]
        l,r = 0,1

        while r < n:
            if cur >= 0:
                l = r
                cur = nums[r]
            else:
                cur += nums[r]
            
            worst = min(worst, cur)
            r += 1
        
        if best < 0:
            return best
        
        return max(best, s-worst)