class MedianFinder:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.same = True

    def addNum(self, num: int) -> None:
        if self.heap2 and num > self.heap2[0]:
            heapq.heappush(self.heap2, num)

            if self.same:
                heapq.heappush(self.heap1, -heapq.heappop(self.heap2))
                self.same = False
            else:
                self.same = True

        else:
            heapq.heappush(self.heap1, -num)

            if self.same:    
                self.same = False
            else:
                heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
                self.same = True

    def findMedian(self) -> float:
        if self.same:
            return (self.heap2[0] - self.heap1[0]) / 2  

        return -self.heap1[0]