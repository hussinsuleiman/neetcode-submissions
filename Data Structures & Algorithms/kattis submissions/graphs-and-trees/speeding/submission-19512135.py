n = int(input())
t_prev, d_prev = map(int, input().split())
best = 0

for i in range(n-1):
    t,d = map(int, input().split())
    best = max(best, (d-d_prev)//(t-t_prev))
    t_prev, d_prev = t,d

print(best)