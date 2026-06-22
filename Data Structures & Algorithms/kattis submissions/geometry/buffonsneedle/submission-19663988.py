n = int(input())
nb = 0

for _ in range(n):
    x1, y1, x2, y2 = map(float, input().split())
    k = int(min(x1, x2))
    
    if (min(x1, x2) <= k+1 and k+1 <= max(x1, x2)) or (min(x1, x2) <= k and k <= max(x1, x2)):
        nb += 1

print(2*n/nb)