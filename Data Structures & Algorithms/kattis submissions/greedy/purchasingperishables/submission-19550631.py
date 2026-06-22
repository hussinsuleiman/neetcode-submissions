N = int(input())
p = list(map(int, input().split()))
best = float('inf')

for jump in range(1, N+1):
    cur = 0
    
    for k in range(0, N, jump):
        cur += p[k]*min(jump, N-k)
    
    best = min(best, cur)

print(best)