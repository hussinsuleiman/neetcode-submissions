class MedianFinder:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.len1 = 0
        self.len2 = 0

    def addNum(self, num: int) -> None:
        if self.len1 == 0:
            heapq.heappush(self.heap1, -num)
            self.len1 += 1
            return

        if self.len1 == self.len2:
            if self.heap2[0] <= num:
                heapq.heappush(self.heap1, -heapq.heappop(self.heap2))
                heapq.heappush(self.heap2, num)
            else:
                heapq.heappush(self.heap1, -num)

            self.len1 += 1

        else:
            if -self.heap1[0] <= num:
                heapq.heappush(self.heap2, num)
            else:
                heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
                heapq.heappush(self.heap1, -num)
            
            self.len2 += 1

    def findMedian(self) -> float:
        if self.len1 > self.len2:
            return -self.heap1[0]
        else:
            return (-self.heap1[0] + self.heap2[0])/2
        