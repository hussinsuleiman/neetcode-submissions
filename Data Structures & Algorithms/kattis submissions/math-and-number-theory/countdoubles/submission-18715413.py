import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nbs = list(map(int, input().split()))
i = 0
nbEven = 0
result = 0

for k in range(i, i+m):
    if nbs[k] % 2 == 0:
        nbEven += 1

for k in range(n - m + 1):
    if nbEven >= 2:
        result += 1
    
    if nbs[i] % 2 == 0:
        nbEven -= 1
    
    if i+m < n and nbs[i+m] % 2 == 0:
        nbEven += 1
    
    i += 1

print(result)