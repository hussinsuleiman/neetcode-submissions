class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = [0]*26
        lettersT = [0]*26

        for letter in s:
            lettersS[ord(letter)-ord('a')] += 1
        for letter in t:
            lettersT[ord(letter)-ord('a')] += 1
        
        for i in range(26):
            if lettersS[i] != lettersT[i]:
                return False
        
        return True