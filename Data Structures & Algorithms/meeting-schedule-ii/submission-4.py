"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:           
        n = len(intervals)
        
        if n == 0:
            return 0

        arr = []

        for interval in intervals:
            arr.append((interval.start, interval.end))
        
        arr.sort()
        ends = [arr[0][1]]
        heapq.heapify(ends)

        for i in range(1, n):
            if arr[i][0] >= ends[0]:
                heapq.heappop(ends)
            heapq.heappush(ends, arr[i][1])

        return len(ends)