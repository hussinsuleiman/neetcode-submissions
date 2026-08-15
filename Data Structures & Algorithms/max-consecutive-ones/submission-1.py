class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        best = 0

        for n in nums:
            if n == 1:
                cur += 1
            else:
                best = max(best, cur)
                cur = 0

        return max(cur, best)