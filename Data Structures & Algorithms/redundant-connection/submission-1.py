class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [set() for i in range(n+1)]

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs():
            seen = set()
            stack = [1]

            while stack:
                top = stack.pop()
                seen.add(top)

                for nei in graph[top]:
                    if nei not in seen:
                        stack.append(nei)
            
            return len(seen) == n
        
        for i in range(n-1, -1, -1):
            a,b = edges[i]
            graph[a].remove(b)
            graph[b].remove(a)

            if dfs():
                return [a,b]
            
            graph[a].add(b)
            graph[b].add(a)