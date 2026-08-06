class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for f,t in tickets:
            graph[f].append(t)

        res = []

        def visit(airport):            
            while graph[airport]:
                nxt = ''

                for nei in graph[airport]:
                    if not nxt or nei < nxt:
                        nxt = nei
                
                graph[airport].remove(nxt)
                visit(nxt)
            
            res.append(airport) 

        visit('JFK')
        return res[::-1]