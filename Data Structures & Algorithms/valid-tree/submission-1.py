class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n-1:
            return False

        edgeSet = {c : [] for c in range(n)}
        visit = set()
        queue = [0]

        for i, j in edges:
            edgeSet[i].append(j)
            edgeSet[j].append(i)
        
        def bfs():
            k = queue.pop(0);

            if k in visit:
                return
            
            visit.add(k)

            for m in edgeSet[k]:
                queue.append(m)
        
        while len(queue) > 0:
            bfs()
        
        return len(visit) == n


