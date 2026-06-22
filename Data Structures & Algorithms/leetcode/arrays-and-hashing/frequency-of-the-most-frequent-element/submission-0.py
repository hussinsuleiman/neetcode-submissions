class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0,1
        l = len(nums)
        res = 1
        nbInc = 0

        while j < l:
            while j < l and (j-i) * (nums[j]-nums[j-1]) + nbInc <= k:
                nbInc += (j-i) * (nums[j]-nums[j-1])
                j += 1
            
            res = max(res, j-i)
            nbInc -= nums[j-1]-nums[i]
            i += 1

        return max(res, j-i)