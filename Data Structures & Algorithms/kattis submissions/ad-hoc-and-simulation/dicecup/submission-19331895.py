N,M = map(int, input().split())
m,n = min(N,M), max(N,M)

for i in range(m+1, n+2):
    print(i)