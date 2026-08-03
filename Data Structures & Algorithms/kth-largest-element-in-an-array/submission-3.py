class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        size = 0

        for n in nums:
            heapq.heappush(heap, n)
            size += 1

            if size > k:
                size -= 1
                heapq.heappop(heap)
        
        return heap[0]