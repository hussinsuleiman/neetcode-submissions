class Solution:
    def pal(self, s):
        l,r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.pal(s[l+1:r+1]) or self.pal(s[l:r])

        return True