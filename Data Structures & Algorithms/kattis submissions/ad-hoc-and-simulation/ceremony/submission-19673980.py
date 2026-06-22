n = int(input())
h = list(map(int, input().split()))
h.sort()
res = 0
i = 0

while i < n:
    i += 1
    res += 1
    
    while i < n and h[i] <= res:
        i += 1

print(res)