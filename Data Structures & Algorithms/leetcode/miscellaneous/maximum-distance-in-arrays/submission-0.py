class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = []
        maxes = []
        m, M = 10000, -10000
        mIndex, MIndex = 0, 0

        for i in range(len(arrays)):
            a = arrays[i]
            mins.append(a[0])
            maxes.append(a[-1])

            if a[0] < m:
                mIndex = i
                m = a[0]

            if a[-1] > M:
                MIndex = i
                M = a[-1]

        if mIndex != MIndex:
            return M-m
        
        mins.remove(m)
        maxes.remove(M)
        m1, M1 = min(mins), max(maxes)

        return max(M1-m, M-m1)

