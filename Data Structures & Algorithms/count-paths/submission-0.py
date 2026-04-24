class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < m:
            n,m = m,n
        
        p = 1

        for i in range(m+n-2, n-1, -1):
            p *= i
        
        f = 1

        for i in range(2, m):
            f *= i

        return p // f