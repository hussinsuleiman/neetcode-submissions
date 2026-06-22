n,b = map(int, input().split())
res = 1

for i in range(b):
    res *= (n-i) / (n+i+1)

print(res**2)