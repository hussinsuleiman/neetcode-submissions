class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        cons = 0
        cur = ''

        for elt in num:
            if elt == cur:
                cons += 1

                if cons == 3:
                    res = max(res, cur*3)
                    cons = 0
            else:
                cons = 1
                cur = elt
        
        return res
