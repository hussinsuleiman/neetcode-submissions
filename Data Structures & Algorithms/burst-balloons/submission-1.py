class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        for k in range(n):
            for i in range(n-k):
                right = nums[i-1] if i > 0 else 1
                left = nums[i+k+1] if i+k+1 < n else 1

                for j in range(i, i+k+1):  
                    dpLeft = dp[i][j-1] if j > i else 0
                    dpRight = dp[j+1][i+k] if j+1 <= i+k else 0
                    dp[i][i+k] = max(dp[i][i+k], nums[j] * right * left + dpLeft + dpRight) 

        return dp[0][n-1]