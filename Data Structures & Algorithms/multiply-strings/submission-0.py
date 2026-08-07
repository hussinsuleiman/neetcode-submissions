class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2 = 0,0

        for n in num1:
            n1 = 10*n1 + ord(n) - ord('0')
        
        for n in num2:
            n2 = 10*n2 + ord(n) - ord('0')
        
        p = n1*n2
        return str(p)