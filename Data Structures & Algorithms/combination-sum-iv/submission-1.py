class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]

        for i in range(1, target+1):
            t = 0

            for nb in nums:
                if nb <= i:
                    t += dp[i-nb]
            
            dp.append(t)

        return dp[-1]