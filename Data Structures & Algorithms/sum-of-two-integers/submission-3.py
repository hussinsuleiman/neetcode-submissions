class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        max_int = (1 << 31) - 1

        while b != 0:
            partial_sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a = partial_sum
            b = carry

        if a <= max_int:
            return a
        
        return ~(a ^ mask)