class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s)-1

        while i < j:
            if not ((ord('0') <= ord(s[i]) and ord(s[i]) <= ord('9')) or (ord('a') <= ord(s[i]) and ord('z') >= ord(s[i]))):
                i += 1
                continue
            
            if not ((ord('0') <= ord(s[j]) and ord(s[j]) <= ord('9')) or (ord('a') <= ord(s[j]) and ord('z') >= ord(s[j]))):
                j -= 1
                continue
            
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            print(i,j)

        return True