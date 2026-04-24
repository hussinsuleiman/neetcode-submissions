class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ind = [0] * 26

        for i in range(26):
            ind[ord(keyboard[i])-ord('a')] = i
        
        t = ind[ord(word[0])-ord('a')]

        for i in range(len(word)-1):
            t += abs(ind[ord(word[i+1])-ord('a')] - ind[ord(word[i])-ord('a')])
        
        return t