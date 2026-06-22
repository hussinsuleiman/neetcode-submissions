N,M = map(int, input().split())
res = 0
cur = 0
detectors = []

for i in range(N):
    P,C = map(int, input().split())
    detectors.append((P,C))  

detectors.sort()

for i in range(N):
    P,C = detectors[i]
    res += max(0, C-cur)
    cur = C

print(res)