class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL = 0
        resR = 0
        cur = 1
        prev = [0]
        n = len(s)

        for i in range(1, n):
            new = [i]

            if s[i-1] == s[i]:
                new.append(i-1)

                if 2 > cur:
                    cur = 2
                    resL = i-1
                    resR = i

            for left in prev:
                if left > 0 and s[left-1] == s[i]:
                    new.append(left-1)

                    if i-left+2 > cur:
                        cur = i-left+2
                        resL = left-1
                        resR = i
            
            prev = new
        
        return s[resL:resR+1]