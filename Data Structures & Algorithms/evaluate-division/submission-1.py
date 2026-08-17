class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)

        for i in range(n):
            a,b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))

        res = []

        for u,v in queries:
            if (u not in graph) or (v not in graph):
                res.append(-1)
                continue
            
            stack = [u]
            seen = {u: 1}

            while stack:
                var = stack.pop()
                prod = seen[var]

                for nei, p in graph[var]:
                    if nei not in seen:
                        stack.append(nei)
                        seen[nei] = p*prod
            
            if v not in seen:
                res.append(-1)
            else:
                res.append(seen[v])
        
        return res