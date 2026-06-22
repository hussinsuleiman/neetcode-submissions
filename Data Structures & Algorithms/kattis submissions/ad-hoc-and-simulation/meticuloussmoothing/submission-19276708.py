n = int(input())
k = list(map(int, input().split()))
total = 0

for i in range(1, n):
    if k[i] > k[i-1]+1:
        total += k[i]-k[i-1]-1
        k[i] -= k[i]-k[i-1]-1

for i in range(n-1, 0, -1):
    if k[i-1] > k[i]+1:
        total += k[i-1]-k[i]-1
        k[i-1] -= k[i-1]-k[i]-1

print(total)