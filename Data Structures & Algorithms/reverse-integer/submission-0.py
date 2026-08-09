class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)
        rev = 0

        while x > 0:
            rev = rev*10 + x%10
            x = x // 10

        if neg:
            rev *= -1
        
        p = 2**31
        return rev if rev >= -p and rev < p else 0 