N,P = map(int, input().split())
T = list(map(int, input().split()))
s,m = sum(T), max(T)
print(s+m*(P-1))