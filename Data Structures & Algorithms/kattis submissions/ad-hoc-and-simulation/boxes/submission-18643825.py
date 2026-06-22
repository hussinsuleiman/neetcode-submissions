import sys
input = sys.stdin.readline
      
N = int(input())
ints = list(map(int, input().split()))
Q = int(input())
adjList = {i: [] for i in range(1, N+1)}

for i in range(N):
    if ints[i] != 0:
        adjList[ints[i]].append(i+1)

for i in range(Q):
    nbs = list(map(int, input().split()))
    visited = set()
    
    for j in range(1, nbs[0]+1):
        visited.add(nbs[j])
        toVisit = [nbs[j]]
        
        while toVisit:
            k = toVisit.pop()
            
            for elt in adjList[k]:
                if elt not in visited:
                    visited.add(elt)
                    toVisit.append(elt)
        
    print(len(visited))


    


