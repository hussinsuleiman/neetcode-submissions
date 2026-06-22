class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [points[0]]
        n,m = len(points), len(points[0])

        for i in range(1, n):
            new = []

            for j in range(m):
                toAdd = 0

                for k in range(m):
                    toAdd = max(toAdd, dp[i-1][k] - abs(j-k))

                new.append(points[i][j] + toAdd)

            dp.append(new)

        return max(dp[-1])    