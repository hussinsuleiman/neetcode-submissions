class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m,M = nums[0],nums[0]
        n = len(nums)
        res = nums[0]

        for i in range(1,n):
            if nums[i] == 0:
                m = 0
                M = 0
            
            elif nums[i] > 0:
                M = max(nums[i], M * nums[i])
                m = min(nums[i], m * nums[i])
            
            else:
                temp = M
                M = max(nums[i], m * nums[i])
                m = min(nums[i], temp * nums[i])
            
            res = max(res, M)
        
        return res