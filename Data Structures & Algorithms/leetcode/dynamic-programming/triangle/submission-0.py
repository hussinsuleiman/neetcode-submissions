class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0]]
        l = len(triangle)

        for i in range(1, l):
            new = [0] * (i+1)
            new[0] = triangle[i][0] + dp[-1][0]
            new[-1] = triangle[i][-1] + dp[-1][-1]

            for j in range(1, i):
                new[j] = triangle[i][j] + min(dp[-1][j-1], dp[-1][j])
            
            dp.append(new)
        
        return min(dp[-1])