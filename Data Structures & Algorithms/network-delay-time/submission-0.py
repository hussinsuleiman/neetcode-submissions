class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        delay = [float('inf')]*(n+1)
        delay[k] = 0
        graph = [[] for i in range(n+1)]

        for u,v,t in times:
            graph[u].append((v,t))

        queue = deque([k])

        while queue:
            top = queue.popleft()
            seen.add(top)

            for v,t in graph[top]:
                if delay[v] > t + delay[top]:
                    delay[v] = delay[top] + t
                    queue.append(v)
            
        return max(delay[1:]) if len(seen) == n else -1