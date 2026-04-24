import heapq

class KthLargest:
    nb = 0
    heap = []

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.nb = k
        heapq.heapify(self.heap)

        for i in range(len(nums)-k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) > 0 and val <= self.heap[0]:
            return self.heap[0]
        else:
            if len(self.heap) >= self.nb:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]

