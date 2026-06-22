class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l+1)
        dp[l] = True
        elts = set(wordDict)

        for i in range(l-1, -1, -1):
            for j in range(i+1, l+1):
                if s[i:j] in elts and dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]