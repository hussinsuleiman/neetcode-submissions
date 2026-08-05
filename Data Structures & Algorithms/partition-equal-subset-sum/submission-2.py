class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s%2 == 1:
            return False

        dp = [False] * (s//2+1)
        dp[0] = True

        for nb in nums:
            new = dp[:]

            for i in range(s//2+1):
                if dp[i]:
                    new[min(i + nb, s - i - nb)] = True
            
            dp = new
        
        return dp[-1]