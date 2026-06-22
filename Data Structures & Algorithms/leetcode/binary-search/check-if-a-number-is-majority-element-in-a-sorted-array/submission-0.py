class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = len(nums)
        first = 0
        i,j = 0,l-1

        while i <= j:
            m = (i+j) // 2

            if nums[m] >= target:
                j = m-1
            else:
                i = m+1
        
        first = i
        last = 0
        i,j = 0,l-1

        while i <= j:
            m = (i+j) // 2

            if nums[m] <= target:
                i = m+1
            else:
                j = m-1
        
        last = j
        return 2*(last-first+1) > l

