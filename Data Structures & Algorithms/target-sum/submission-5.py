class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        s = sum(nums)
        m = max(s, target)
        dp = [0] * (2*m+1)
        dp[m] = 1
        
        for i in range(l):
            new = [0] * (2*m+1)

            for j in range(2*m+1):
                if j >= nums[i]:
                    new[j] += dp[j-nums[i]]

                if j <= 2*m-nums[i]:
                    new[j] += dp[j+nums[i]]

            dp = new

        return dp[m+target]   