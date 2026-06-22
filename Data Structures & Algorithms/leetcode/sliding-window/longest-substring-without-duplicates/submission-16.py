class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = dict()
        i = 0
        j = 0
        maxLen = 0

        while j < len(s):
            if s[j] in chars.keys():
                maxLen = max(maxLen, j-i)
                i = max(i, chars[s[j]] + 1)
                
            chars[s[j]] = j
            j += 1

        return max(maxLen, j-i)