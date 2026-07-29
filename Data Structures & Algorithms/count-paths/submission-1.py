class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact = [1]

        for i in range(1, m+n-1):
            fact.append(fact[-1] * i)

        return fact[m+n-2] // fact[n-1] // fact[m-1]