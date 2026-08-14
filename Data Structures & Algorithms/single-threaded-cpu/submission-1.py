class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        n = len(tasks)
        taskId = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        taskId.sort()
        time = taskId[0][0]
        heap = []
        i = 0

        while len(res) < n:
            while i < n and taskId[i][0] <= time:
                heapq.heappush(heap, (taskId[i][1], taskId[i][2]))
                i += 1
            
            if not heap:
                time = taskId[i][0]
                continue
            
            processTime, ind = heapq.heappop(heap)
            res.append(ind)
            time += processTime

        return res