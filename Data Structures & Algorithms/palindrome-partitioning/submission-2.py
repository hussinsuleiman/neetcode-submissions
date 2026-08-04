class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        n = len(s)

        def backtrack(idx):
            if idx == n:
                res.append(cur.copy())
                return
            
            for i in range(idx, n):
                l,r = idx, i

                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        r -= 1
                    else:
                        break
                
                if l >= r:
                    cur.append(s[idx:i+1])
                    backtrack(i+1)
                    cur.pop()

        backtrack(0)
        return res