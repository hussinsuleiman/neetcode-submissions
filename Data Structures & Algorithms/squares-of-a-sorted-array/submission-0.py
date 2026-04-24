class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg, pos = [], []
        i = 0
        l = len(nums)

        while i < l and nums[i] < 0:
            neg.append(nums[i]**2)
            i += 1

        while i < l:
            pos.append(nums[i]**2)
            i += 1

        k = len(neg)
        n,p = k-1,0
        out = []

        while n > -1 and p < l-k:
            if neg[n] < pos[p]:
                out.append(neg[n])
                n -= 1
            else:
                out.append(pos[p])
                p += 1
        
        if n == -1:
            for i in range(p, l-k):
                out.append(pos[i])
        
        elif p == l-k:
            for i in range(n, -1, -1):
                out.append(neg[i])
        
        return out
