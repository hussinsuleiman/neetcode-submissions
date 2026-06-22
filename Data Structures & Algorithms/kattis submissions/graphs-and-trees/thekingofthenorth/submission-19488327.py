import sys
from collections import deque

input = sys.stdin.readline
INF = 10**18

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0

        while q:
            u = q.popleft()
            for v, cap, _ in self.g[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)

        return self.level[t] != -1

    def dfs(self, u, t, f):
        if u == t:
            return f
        while self.it[u] < len(self.g[u]):
            i = self.it[u]
            v, cap, rev = self.g[u][i]

            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, t, min(f, cap))
                if pushed:
                    self.g[u][i][1] -= pushed
                    self.g[v][rev][1] += pushed
                    return pushed

            self.it[u] += 1

        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if pushed == 0:
                    break
                flow += pushed
        return flow


def solve():
    R, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    cr, cc = map(int, input().split())

    def in_id(r, c):
        return 2 * (r * C + c)

    def out_id(r, c):
        return 2 * (r * C + c) + 1

    N = 2 * R * C + 2
    S = N - 2
    T = N - 1
    mf = Dinic(N)

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue
            mf.add_edge(in_id(r, c), out_id(r, c), grid[r][c])

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 0:
                    mf.add_edge(out_id(r, c), in_id(nr, nc), INF)


    mf.add_edge(S, in_id(cr, cc), INF)

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                mf.add_edge(out_id(r, c), T, INF)

    print(mf.max_flow(S, T))

solve()