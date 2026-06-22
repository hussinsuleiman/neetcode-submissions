N = int(input())
a = list(map(int, input().split()))
total = 0

for i in range(N-1):
    total += max(0, a[i]-a[i+1]-1)
    
total += a[-1]-1
print(total)