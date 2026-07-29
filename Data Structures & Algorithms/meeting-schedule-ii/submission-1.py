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
        arr = []

        for interval in intervals:
            arr.append((interval.start, interval.end))
        
        arr.sort()
        ends = []
        res = 0
        cur = 0

        for i in range(n):
            done = False

            for j in range(cur):
                end = ends[j]

                if arr[i][0] >= end:
                    ends[j] = arr[i][1]
                    done = True
                    break
            
            if done:
                continue
            
            ends.append(arr[i][1])
            cur += 1
            res = max(res, cur)
        
        return res