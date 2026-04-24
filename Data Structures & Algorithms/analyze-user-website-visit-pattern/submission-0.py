class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        visited = defaultdict(list)

        for i in range(n):
            visited[username[i]].append((timestamp[i], website[i]))
        
        for elt in visited.keys():
            visited[elt].sort()
        
        patterns = defaultdict(int)

        for elt in visited.keys():
            i = 0
            l = len(visited[elt])

            while i+2 < l:
                patterns[(visited[elt][i][1], visited[elt][i+1][1], visited[elt][i+2][1])] += 1
                i += 1
        
        out = []
        occMax = 0

        for a,b,c in patterns.keys():
            if patterns[(a,b,c)] > occMax:
                occMax = patterns[(a,b,c)]
                out = [a,b,c]
            
            elif patterns[(a,b,c)] == occMax:
                if a < out[0] or (a == out[0] and b < out[1]) or (a == out[0] and b == out[1] and c < out[2]):
                    out = [a,b,c]
        
        return out