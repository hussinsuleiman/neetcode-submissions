class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)

        for i in range(l//2):
            s[i], s[l-1-i] = s[l-1-i], s[i]

        spaces = [-1]

        for i in range(l):
            if s[i] == ' ':
                spaces.append(i)
        
        spaces.append(l)
        L = len(spaces)

        for i in range(L-1):
            k = spaces[i+1] - spaces[i]

            for j in range(k//2):
                s[j+spaces[i]+1], s[spaces[i+1]-1-j] = s[spaces[i+1]-1-j], s[j+spaces[i]+1]
            
        return s


