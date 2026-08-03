class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        heap = [-stones[i] for i in range(n)]
        heapq.heapify(heap)
        i = 0

        while i < n-1:
            a,b = -heapq.heappop(heap), -heapq.heappop(heap)

            if a == b:
                i += 2
            else:
                i += 1
                heapq.heappush(heap, b-a)

        return -heap[0] if heap else 0