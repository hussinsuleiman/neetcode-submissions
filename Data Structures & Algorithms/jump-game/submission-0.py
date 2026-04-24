class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [False] * l
        dp[l-1] = True

        for i in range(l-2, -1, -1):
            for j in range(i+1, i+nums[i]+1):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]