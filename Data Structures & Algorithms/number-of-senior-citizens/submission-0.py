class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for c in details:
            if int(c[11:13]) > 60:
                res += 1
        
        return res