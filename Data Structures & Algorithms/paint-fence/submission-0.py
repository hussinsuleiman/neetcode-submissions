class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        one_back = k*k
        two_back = k

        for i in range(3, n+1):
            new = (k-1) * (one_back + two_back)
            two_back = one_back
            one_back = new
        
        return one_back