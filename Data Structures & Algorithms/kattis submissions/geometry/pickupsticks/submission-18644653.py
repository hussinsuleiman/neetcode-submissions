import sys
from collections import deque, defaultdict

input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split())
adj = defaultdict(list)
in_deg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    in_deg[b] += 1

q = deque(i for i in range(1, n + 1) if in_deg[i] == 0)
order = []

while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            q.append(v)

if len(order) == n:
    write("\n".join(map(str, order)))
else:
    write("IMPOSSIBLE\n")


            
    