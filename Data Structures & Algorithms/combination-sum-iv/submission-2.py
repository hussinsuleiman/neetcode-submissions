class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [[0] * (len(nums)+1) for i in range(target+1)]

        for j in range(len(nums)+1):
            dp[0][j] = 1

        for i in range(1, target+1):
            for j in range(1, len(nums)+1):
                for k in range(j):
                    if i >= nums[k]:
                        dp[i][j] += dp[i - nums[k]][j]
        
        return dp[target][len(nums)]