class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        d = defaultdict(list)
        l = len(x)

        for i in range(l):
            d[x[i]].append(y[i])
        
        if len(d.keys()) < 3:
            return -1
        
        top = []
        heapq.heapify(top)

        for elt in d:
            heapq.heappush(top, -max(d[elt]))
        
        res = 0

        for i in range(3):
            res -= top[0]
            heapq.heappop(top)

        return res