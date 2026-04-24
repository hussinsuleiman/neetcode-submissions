class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i = 0
        j = 0
        a = len(word1)
        b = len(word2)

        while i < a and j < b:
            if i == j:
                output.append(word1[i])
                i += 1
            else:
                output.append(word2[j])
                j += 1

        if i == a:
            for k in range(j, b):
                output.append(word2[k])
        else:
            for k in range(i, a):
                output.append(word1[k])
        
        return ''.join(output)