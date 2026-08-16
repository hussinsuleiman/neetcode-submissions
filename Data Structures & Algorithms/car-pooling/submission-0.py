class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        new = [(trip[1], trip[2], trip[0]) for trip in trips]
        new.sort()
        cur = 0
        i = 0
        heap = []

        while i < len(trips):
            while heap and heap[0][0] <= new[i][0]:
                t, nb = heapq.heappop(heap)
                cur -= nb

            if cur + new[i][2] > capacity:
                return False

            cur += new[i][2]
            heapq.heappush(heap, (new[i][1], new[i][2]))
            i += 1

        return True