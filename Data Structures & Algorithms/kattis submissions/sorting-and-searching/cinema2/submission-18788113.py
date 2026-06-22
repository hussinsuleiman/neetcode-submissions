import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nbs = list(map(int, input().split()))
i = 0

while nbs[i] <= N:
    N -= nbs[i]
    i += 1

print(M-i)