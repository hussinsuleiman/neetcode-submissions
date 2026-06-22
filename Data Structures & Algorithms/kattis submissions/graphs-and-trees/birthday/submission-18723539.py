import sys
input = sys.stdin.readline

p, c = map(int, input().split())

while (p,c) != (0,0):
    adjList = {i: [] for i in range(p)}
    
    for i in range(c):
        a,b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    
    disc = [-1] * p
    low = [-1] * p
    time = [0]
    found_bridge = [False]

    def dfs(u, parent):
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in adjList[u]:
            if v == parent:
                continue

            if disc[v] == -1:  # tree edge
                dfs(v, u)
                low[u] = min(low[u], low[v])

                # Bridge condition
                if low[v] > disc[u]:
                    found_bridge[0] = True

            else:  # back edge
                low[u] = min(low[u], disc[v])

    # Start DFS from node 0
    dfs(0, -1)

    # Must also be connected
    if any(d == -1 for d in disc):  
        print("Yes")

    else:
        if not found_bridge[0]:
            print("No")
        else:
            print("Yes")
    
    p, c = map(int, input().split())