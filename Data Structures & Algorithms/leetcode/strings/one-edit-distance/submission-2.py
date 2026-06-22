class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        a,b = len(s), len(t)

        if a == b:
            d = 0

            for i in range(a):
                if s[i] != t[i]:
                    d += 1
                    if d == 2:
                        return False
            
            return d == 1
        
        elif abs(a-b) > 1:
            return False

        elif a-b == 1:
            s,t = t,s
            a,b = b,a
        
        i = 0

        while i < a and s[i] == t[i]:
            i += 1
               
        while i < a and s[i] == t[i+1]:
            i += 1
        
        return i >= a