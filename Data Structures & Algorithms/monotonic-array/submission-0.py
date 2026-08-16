class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i < n-1 and nums[i+1] == nums[i]:
            i += 1
        
        if i == n-1:
            return True

        inc = nums[i+1] > nums[i]
        i += 1

        while i < n-1:
            if (nums[i+1] > nums[i] and not inc) or (nums[i+1] < nums[i] and inc):
                return False
            i += 1
        
        return True