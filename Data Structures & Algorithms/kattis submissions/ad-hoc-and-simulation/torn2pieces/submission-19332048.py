from collections import defaultdict

N = int(input())
adjList = defaultdict(set)

for i in range(N):
    stations = input().split()
    
    for j in range(1, len(stations)):
        adjList[stations[0]].add(stations[j])
        adjList[stations[j]].add(stations[0])

start, end = map(str, input().split())
visited = set([start])
stack = [(start, [start])]

while stack:
    station, prev = stack.pop()
    
    if station == end:
        print(' '.join(prev))
        exit()
    
    for nei in adjList[station]:
        if nei not in visited:
            stack.append((nei, prev + [nei]))
            visited.add(nei)

print("no route found")