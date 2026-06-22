class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        l = len(nums)

        for i in range(1, l):
            r = 1

            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    r = max(r, 1 + dp[j])
            
            dp.append(r)
        
        return max(dp)