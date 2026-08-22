class Solution:
    def minEnd(self, n: int, x: int) -> int:
        idx = []
        bin_x = bin(x)[2:]
        bin_n = bin(n-1)[2:]
        pos = []
        nb = int(bin_x, 2)
        l = len(bin_n)
        i = 0

        while len(pos) < l:
            if nb % 2 == 0:
                pos.append(i)
            nb //= 2
            i += 1
        
        res = x

        for i in range(len(bin_n)-1, -1, -1):
            if bin_n[i] == '1':
                res += 2**pos[len(bin_n)-1-i] 

        return res