class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for i in range(numCourses)]

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            top = queue.popleft()
            order.append(top)

            for nei in graph[top]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        return [] if len(order) < numCourses else order