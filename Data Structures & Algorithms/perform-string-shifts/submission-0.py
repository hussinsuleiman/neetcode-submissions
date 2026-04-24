class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        t = 0

        for a,b in shift:
            t += b * (-1)**(a)
        
        out = []

        for i in range(t, t+len(s)):
            out.append(s[i%len(s)])
        
        return ''.join(out)
            