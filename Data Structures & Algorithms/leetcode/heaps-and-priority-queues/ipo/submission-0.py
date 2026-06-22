class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        capital_heap = [(capital[i], profits[i]) for i in range(n)]
        heapq.heapify(capital_heap)
        profit_heap = []

        for i in range(k):
            while capital_heap and capital_heap[0][0] <= w:
                _, profit = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, -profit)
            
            if not profit_heap:
                break

            w -= heapq.heappop(profit_heap)

        return w