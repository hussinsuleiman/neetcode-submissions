class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            if a < b:
                heapq.heappush(stones, a-b)
            elif a > b:
                heapq.heappush(stones, b-a)
        
        if not stones:
            return 0
        return -stones[0]


