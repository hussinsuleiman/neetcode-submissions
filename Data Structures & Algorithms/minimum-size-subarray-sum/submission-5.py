class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0
        i,j = 0,0
        res = float('inf')

        while j < len(nums):
            while j < len(nums) and cur < target:
                cur += nums[j]
                j += 1
            
            while cur >= target:
                res = min(res, j-i) 
                cur -= nums[i]
                i += 1
            
            if i == j:
                return 1

        return 0 if res == float('inf') else res