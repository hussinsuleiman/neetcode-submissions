class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [nums[0]]

        for i in range(1, l):
            r = nums[i]
            cur = r

            for j in range(i-1, -1, -1):
                cur *= nums[j]
                r = max(cur, r)

            dp.append(max(r, dp[i-1]))
        
        return dp[l-1]
        

        
    