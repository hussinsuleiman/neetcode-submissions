class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(' ')
        i = -1

        while not a[i]:
            i -= 1

        return len(a[i]) 
        