class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        i = 0
        res = 0

        while i < n-1:
            if intervals[i][1] > intervals[i+1][0]:
                res += 1
                intervals[i+1][1] = min(intervals[i+1][1], intervals[i][1])
            i += 1
        
        return res