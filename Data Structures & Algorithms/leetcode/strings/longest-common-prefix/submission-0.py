class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        prefix = self.longestCommonPrefix(strs[:-1])
        lastWord = strs[-1]
        output = ''

        for i in range(min(len(prefix), len(lastWord))):
            if lastWord[i] == prefix[i]:
                output += prefix[i]
            else:
                break
        
        return output