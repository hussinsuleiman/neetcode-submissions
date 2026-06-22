n,t = map(float, input().split())
n = int(n)
a = list(map(float, input().split()))
res = 0

for x in a:
    res += (t**2-(x/2)**2)**0.5

print(res)