class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s, i, j, length):
            a, b = j, j+i

            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            
            return True
        
        length = len(s)

        for i in range(length-1, -1, -1):
            for j in range(length-i):
                if isPalindrome(s, i, j, length):
                    return s[j:j+i+1]

