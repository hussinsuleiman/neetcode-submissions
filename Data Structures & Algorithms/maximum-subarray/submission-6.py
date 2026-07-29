class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        idx = 0
        n = len(nums)

        while idx < n:
            if cur < 0:
                cur = nums[idx]
            else:
                cur += nums[idx]
            
            idx += 1
            res = max(res, cur)
        
        if res == 0:
            return max(nums)
        
        return res