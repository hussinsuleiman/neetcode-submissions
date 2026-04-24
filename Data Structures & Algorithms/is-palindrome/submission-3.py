class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return (ord('0') <= ord(c) <= ord('9')) or (ord('a') <= ord(c) <= ord('z'))

        i = 0
        j = len(s)-1
        s = s.lower()

        while i < j:
            if isAlphaNum(s[i]) and isAlphaNum(s[j]) and ord(s[i]) != ord(s[j]):
                return False
            elif isAlphaNum(s[i]) and not isAlphaNum(s[j]):
                j -= 1
            elif isAlphaNum(s[j]) and not isAlphaNum(s[i]):
                i += 1
            else:
                i += 1
                j -= 1

        return True