class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        i = 0

        while i < len(nums)-1:
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            
            if i == len(nums)-1:
                return res

            if nums[i] < nums[i+1]:
                cur = 2
                i += 1

                while i < len(nums)-1 and nums[i] < nums[i+1]:
                    cur += 1
                    i += 1
                
                res = max(res, cur)
            
            else:
                cur = 2
                i += 1

                while i < len(nums)-1 and nums[i] > nums[i+1]:
                    cur += 1
                    i += 1
                
                res = max(res, cur)

        return res