"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = []

        for interval in intervals:
            arr.append((interval.start, interval.end))

        arr.sort()
        n = len(arr)

        for i in range(1, n):
            if arr[i][0] < arr[i-1][1]:
                return False
        
        return True