class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        output = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2

            if len(heap) == k:
                if -heap[0][0] > dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-dist, point])
            else:
                heapq.heappush(heap, [-dist, point])
        
        for [d, pt] in heap:
            output.append(pt)
        
        return output
