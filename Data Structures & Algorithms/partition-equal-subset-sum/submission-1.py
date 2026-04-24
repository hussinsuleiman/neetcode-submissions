class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s%2 != 0:
            return False
        
        q = s // 2
        dp = [False] * (q+1)
        dp[0] = True

        for nb in nums:
            new = dp.copy()

            for i in range(q+1):
                if dp[i] and i + nb <= q:
                    new[i+nb] = True
            
            dp = new
        
        return dp[q]