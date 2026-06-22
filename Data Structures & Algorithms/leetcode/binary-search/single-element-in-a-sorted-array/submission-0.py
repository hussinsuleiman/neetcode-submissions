class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = len(nums)
        i,j = 0, l-1

        while i <= j:
            m = (i+j) // 2

            if m == 0 or m == l-1:
                return nums[m] 

            if nums[m-1] < nums[m] < nums[m+1]:
                return nums[m]

            elif nums[m-1] == nums[m]:
                if m%2 == 0:
                    j = m-2
                else:
                    i = m+1
            
            else:
                if m%2 == 0:
                    i = m+2
                else:
                    j = m-1
        
        return nums[i]