class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, u):
            while u != parent[u]:
                u = parent[u]
            return u
        
        def union(parent, size, u, v):
            p1, p2 = find(parent, u), find(parent, v)

            if p1 == p2:
                return False
            
            if size[p1] < size[p2]:
                p1, p2 = p2, p1
            
            size[p1] += size[p2]
            parent[p2] = p1
            return True

        edges = []
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                w = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((w, i, j))
        
        edges.sort()
        par = [i for i in range(n)]
        size = [1 for i in range(n)]
        nbEdges = 0
        tot = 0
        ind = 0 

        while nbEdges < n-1:
            w,i,j = edges[ind]

            if union(par, size, i, j):
                nbEdges += 1
                tot += w
            
            ind += 1

        return tot