class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        
        def backtrack(i):
            if i == n+1:
                if len(cur) == k:
                    res.append(cur.copy())
                return
            
            if len(cur) < k:
                cur.append(i)
                backtrack(i+1)
                cur.remove(i)

            backtrack(i+1)

        backtrack(1)
        return res