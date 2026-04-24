class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        l = len(stones)
        s = sum(stones)
        dp = [False] * (s//2+1)
        dp[0] = True

        for stone in stones:
            new = dp.copy()

            for i in range(s//2+1-stone):
                if dp[i]:
                    new[i+stone] = True
            
            dp = new
        
        for i in range(s//2, -1, -1):
            if dp[i]:
                return s-2*i