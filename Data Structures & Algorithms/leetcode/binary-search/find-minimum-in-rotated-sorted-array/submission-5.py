class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        i = 0
        j = len(nums)-1

        while i < j-1:
            mid = (i+j) // 2

            if nums[i] < nums[j]:
                return nums[i]

            if nums[mid] < nums[i]:
                j = mid
            else:
                i = mid
        
        return min(nums[i], nums[i+1])