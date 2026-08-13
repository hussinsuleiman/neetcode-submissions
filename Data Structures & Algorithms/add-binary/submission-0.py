class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        l1, l2 = len(a), len(b)
        carry = 0
        i = -1

        while i >= -max(l1,l2):
            n1 = int(a[i]) if i >= -l1 else 0
            n2 = int(b[i]) if i >= -l2 else 0

            res.append(str((n1+n2+carry)%2))
            carry = (n1+n2+carry) // 2
            i -= 1
        
        if carry:
            res.append('1')
        
        res = res[::-1]
        return ''.join(res)