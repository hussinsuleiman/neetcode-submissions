n = int(input())
parts = list(map(float, input().split()))
parts.sort()
res = sum(parts)
cur = 1

for i in range(n-1, -1, -1):
    if cur < parts[i]:
        continue
    
    res += (cur-parts[i])/2
    cur -= (cur-parts[i])/2

print(res)