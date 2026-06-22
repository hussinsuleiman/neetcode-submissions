n = int(input())
res = 0

for _ in range(n):
    u,d = map(int, input().split())
    
    if (d > 10000 or d < 1) and u%8 != 0:
        res += 1

print(res)