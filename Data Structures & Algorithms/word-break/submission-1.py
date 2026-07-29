class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)
        dp = [False]*(n+1)
        dp[0] = True
        L = []

        for word in wordDict:
            L.append(len(word))

        for i in range(n):
            for j in range(m):
                if L[j] <= i+1 and dp[i+1-L[j]] and s[i+1-L[j]:i+1] == wordDict[j]:
                    dp[i+1] = True
                    break
        
        return dp[n]