class Solution:
    def confusingNumber(self, n: int) -> bool:
        digits = []
        digitsRev = []
        s = str(n)

        for c in s:
            if c not in {'0', '1', '6', '8', '9'}:
                return False
            digits.append(c)
        
        for i in range(len(s)-1, -1, -1):
            if digits[i] == '9':
                digitsRev.append('6')
            elif digits[i] == '6':
                digitsRev.append('9')
            else:
                digitsRev.append(digits[i])
        
        for i in range(len(s)):
            if digits[i] != digitsRev[i]:
                return True

        return False
        


