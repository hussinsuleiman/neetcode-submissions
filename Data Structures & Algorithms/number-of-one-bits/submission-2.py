class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        cnt = 0

        for i in range(2, len(b)):
            cnt += (int(b[i]) & 1)
        
        return cnt