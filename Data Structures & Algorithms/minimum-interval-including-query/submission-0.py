class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        qInit = queries[:]
        queries.sort()
        heap = []
        i = 0
        n = len(intervals)
        res = dict()

        for q in queries:
            while i < n and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1
        
        ans = []

        for q in qInit:
            ans.append(res[q])

        return ans