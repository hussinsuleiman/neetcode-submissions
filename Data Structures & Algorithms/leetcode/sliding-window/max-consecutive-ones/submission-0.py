class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        cur = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                m = max(cur, m)
                cur = 0
        
        return max(m, cur)