class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [set() for i in range(numCourses)]
        indegree = [0] * numCourses

        for a,b in prerequisites:
            graph[a].add(b)
            indegree[b] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            top = queue.popleft()
            order.append(top)

            for nei in graph[top]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        preReq = [set() for i in range(numCourses)]

        for i in range(1, numCourses):
            for j in range(i):
                if order[i] in graph[order[j]]:
                    preReq[order[i]].add(order[j])
                    
                    for elt in preReq[order[j]]:
                        preReq[order[i]].add(elt)
            
        ans = []

        for u,v in queries:
            ans.append(u in preReq[v]) 
        
        return ans