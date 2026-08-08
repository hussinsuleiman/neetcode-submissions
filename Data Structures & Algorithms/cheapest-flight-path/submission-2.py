class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        queue = deque([(src, 0)])
        dist = [float('inf')]*n
        dist[src] = 0
        graph = [[] for i in range(n)]

        for u,v,t in flights:
            graph[u].append((v,t))

        while queue:
            top, stops = queue.popleft()

            for nei,t in graph[top]:
                if dist[nei] > dist[top] + t and (not (stops == k and nei != dst)):
                    dist[nei] = dist[top] + t
                    queue.append((nei, stops+1))
        
        return dist[dst] if dist[dst] != float('inf') else -1