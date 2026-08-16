class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        cur = nums[0]
        i = 1

        while i < len(nums):
            if nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                res = max(res, cur)
                cur = nums[i]
            
            i += 1

        return max(res, cur)