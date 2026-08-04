class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])

        while n != 1:
            x = 0

            while n != 0:
                x += (n%10) ** 2
                n //= 10
            
            n = x

            if n in seen:
                return False

            seen.add(n)

        return True