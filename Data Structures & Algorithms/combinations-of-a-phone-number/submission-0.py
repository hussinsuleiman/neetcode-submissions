class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = []
        n = len(digits)
        d = [{'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'}, {'j', 'k', 'l'}, {'m', 'n', 'o'}, {'p', 'q', 'r', 's'}, {'t', 'u', 'v'}, {'w', 'x', 'y', 'z'}]

        def backtrack(idx):
            if idx == n:
                if cur:
                    res.append(''.join(cur))
                return
            
            for elt in d[int(digits[idx])-2]:
                cur.append(elt)
                backtrack(idx+1)
                cur.pop()
        
        backtrack(0)
        return res