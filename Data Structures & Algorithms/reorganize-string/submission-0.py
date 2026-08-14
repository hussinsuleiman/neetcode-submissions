class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        occ = defaultdict(int)

        for c in s:
            occ[c] += 1
        
        heap = [(-occ[c], c) for c in occ]
        heapq.heapify(heap)
        res = []

        while heap:
            occTop, cTop = heapq.heappop(heap)
            res.append(cTop)

            if not heap:
                break
            
            occ2, c2 = heapq.heappop(heap)
            res.append(c2)

            if occTop < -1:
                heapq.heappush(heap, (occTop+1, cTop))
            
            if occ2 < -1:
                heapq.heappush(heap, (occ2+1, c2))
        
        return ''.join(res) if len(res) == n else ''