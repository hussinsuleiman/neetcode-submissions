class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, res = 0, 0
        
        for n in nums:
            if n + cur > 0:
                cur += n
            else:
                cur = 0
            
            res = max(res, cur)

        m = max(res, cur)

        if m > 0:
            return m
        return max(nums)