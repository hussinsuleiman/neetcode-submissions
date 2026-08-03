class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        n = len(nums) 
        self.size = min(n, k)
        self.k = k
        heapq.heapify(self.heap)

        for i in range(n-k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.size += 1

        if self.size > self.k:
            heapq.heappop(self.heap)
            self.size -= 1

        return self.heap[0]