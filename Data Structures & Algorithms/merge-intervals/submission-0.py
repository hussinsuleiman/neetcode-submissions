class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        if n < 2:
            return intervals

        for i in range(n-2, -1, -1):
            if intervals[i][1] >= intervals[n-1][0] and intervals[i][0] <= intervals[n-1][1]:
                intervals[i] = [min(intervals[i][0], intervals[n-1][0]), max(intervals[i][1], intervals[n-1][1])]
                intervals.pop()
                return self.merge(intervals)

        return self.merge(intervals[:-1]) + [intervals[n-1]]