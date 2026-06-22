class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        currSum = 0
        n = len(nums)
        minLen = n+1

        while j <= n:
            if currSum >= target:
                minLen = min(minLen, j-i)
                currSum -= nums[i]
                i += 1
            else:
                if j < n:
                    currSum += nums[j]
                j += 1
        
        if minLen > n:
            return 0

        return minLen
        
                