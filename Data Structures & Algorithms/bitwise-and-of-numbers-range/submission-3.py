class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = bin(left)[2:]
        res = [l[i] for i in range(len(l))]
        comp = 0

        for k in range(len(l)):
            if right - left > comp:
                res[len(l)-1-k] = '0'

            if l[len(l)-1-k] == '0':
                comp += 2**k

        nb = int(''.join(res), 2)
        return nb 