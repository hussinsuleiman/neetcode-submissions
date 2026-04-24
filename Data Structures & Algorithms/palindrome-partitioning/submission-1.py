class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i):
            if i == l:  
                return [[]]

            res = []
            for k in range(i, l):
                if isPalindrome(i, k):
                    for part in dfs(k+1):
                        res.append([s[i:k+1]] + part)
            return res

        return dfs(0)