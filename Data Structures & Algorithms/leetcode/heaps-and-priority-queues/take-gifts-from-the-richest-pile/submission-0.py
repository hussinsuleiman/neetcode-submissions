class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts] 
        heapq.heapify(heap)

        for i in range(k):
            heapq.heappush(heap, -int((-heapq.heappop(heap)) ** 0.5))

        return -sum(heap)