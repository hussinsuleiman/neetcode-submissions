class Solution:
    def climbStairs(self, n: int) -> int:
        nbWays = [0,1,2]

        for i in range(3, n+1):
            nbWays.append(nbWays[i-1] + nbWays[i-2])
        
        return nbWays[n]