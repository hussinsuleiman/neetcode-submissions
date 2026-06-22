import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nbs = list(map(int, input().split()))
total = 0

for i in range(M):
    if nbs[i] <= N:
        N -= nbs[i]
    else:
        total += 1

print(total)