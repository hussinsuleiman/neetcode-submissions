class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i,j = 1, len(nums)
        nums = [-float('inf')] + nums + [-float('inf')]

        while i <= j:
            m = (i+j) // 2

            if nums[m-1] < nums[m] and nums[m+1] < nums[m]:
                return m-1
            
            elif nums[m] <= nums[m-1]:
                j = m-1
            
            else:
                i = m+1