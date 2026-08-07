class Solution:
    def powPos(self, x, n):
        if n == 0:
            return 1
        return min(10**6, x**(n%2) * (self.powPos(x, n//2))**2)   

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.powPos(x, -n)
        return self.powPos(x, n)        