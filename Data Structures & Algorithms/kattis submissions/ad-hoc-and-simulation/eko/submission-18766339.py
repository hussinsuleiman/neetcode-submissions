import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nbs = list(map(int, input().split()))
nbs.sort()
s = sum(nbs)
cur = s
index = 0

while cur > M:
    s -= nbs[index]
    cur = s - nbs[index] * (N-index-1)
    index += 1

index -= 1
res = (M - cur) // (N-index)

if (M - cur) % (N-index) > 0:
    res += 1

print(nbs[index] - res)
    
    

