class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        wordSet = set(words)

        for word in words:
            m = len(word)
            dp = [False] * (m+1)
            dp[0] = True

            for i in range(1, m+1):
                for j in range(i):
                    if i == m and j == 0:
                        continue

                    if dp[j] and word[j:i] in wordSet:
                        dp[i] = True
                        break
        
            if dp[m]:
                res.append(word)
        
        return res    