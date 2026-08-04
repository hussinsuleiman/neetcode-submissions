class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        n = len(candidates)
        candidates.sort()

        def backtrack(idx, s):
            if idx == n:
                if s == target:
                    res.append(cur.copy())
                return
            
            if s > target:
                return

            cur.append(candidates[idx])
            backtrack(idx+1, s + cur[-1])
            cur.pop()
            i = idx+1

            while i < n and candidates[i] == candidates[idx]:
                i += 1

            backtrack(i, s)
        
        backtrack(0, 0)
        return res