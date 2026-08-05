class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 1,1
        n = len(nums)

        while j < n:
            while j < n and nums[j] == nums[i-1]:
                j += 1
            
            if j < n:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
        
        return i