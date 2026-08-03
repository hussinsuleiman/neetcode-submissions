class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        size = 0

        for x,y in points:
            heapq.heappush(heap, (- x**2 - y**2, (x,y)))
            size += 1

            if size > k:
                heapq.heappop(heap)
                size -= 1
        
        res = []

        while heap:
            a,b = heapq.heappop(heap)[1]
            res.append([a,b])
        
        return res