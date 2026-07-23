class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        a = ['0'] * 32
        l = len(b)

        for i in range(2, l):
            a[i-2] = b[l-i+1]
        
        return int(''.join(a), 2)