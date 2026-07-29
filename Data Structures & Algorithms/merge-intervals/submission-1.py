class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        res = [intervals[0]]
        i = 1

        while i < n:
            while i < n and intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                i += 1

            if i < n:
                res.append(intervals[i])
                i += 1
        
        return res