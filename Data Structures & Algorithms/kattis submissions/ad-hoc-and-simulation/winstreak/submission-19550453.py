N = int(input())
cur = 0
l = 0

for _ in range(N):
    S,T = map(int, input().split())
    
    if S > T:
        cur += 1
    else:
        cur = 0
    
    l = max(l, cur)

print(l)