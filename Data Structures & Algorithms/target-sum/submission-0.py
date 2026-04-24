class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [dict()]
        dp[0][0] = 1
        l = len(nums)

        for i in range(l):
            new = defaultdict(int)

            for j in dp[-1]:
                new[j+nums[i]] += dp[-1][j]
                new[j-nums[i]] += dp[-1][j]
            
            dp.append(new)
        
        return dp[-1][target]