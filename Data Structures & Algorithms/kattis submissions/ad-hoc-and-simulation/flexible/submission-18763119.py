import sys
input = sys.stdin.readline

W, P = map(int, input().split())
nbs = list(map(int, input().split()))
nbs = [0] + nbs + [W]
sums = set()

for i in range(P+2):
    for j in range(i+1, P+2):
        sums.add(nbs[j] - nbs[i])

sums = list(sums)
sums.sort()

for i in range(len(sums)):
    sums[i] = str(sums[i])

print(" ".join(sums))

