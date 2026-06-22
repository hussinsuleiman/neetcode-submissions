class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1000] * l
        dp[l-1] = 0

        for i in range(l-2, -1, -1):
            m = 1000

            for j in range(i+1, min(i+nums[i]+1, l)):
                m = min(dp[j]+1, m)
            
            dp[i] = m
        
        return dp[0]