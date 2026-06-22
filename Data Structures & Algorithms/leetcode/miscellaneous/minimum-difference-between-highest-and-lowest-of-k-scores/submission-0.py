class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0,k-1
        res = nums[j]-nums[i]
        l = len(nums)

        while j < l-1:
            j += 1
            i += 1
            res = min(res, nums[j]-nums[i])
        
        return res