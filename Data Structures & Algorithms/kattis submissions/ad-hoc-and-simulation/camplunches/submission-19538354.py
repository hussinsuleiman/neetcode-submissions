n = int(input())
s = list(map(int, input().split()))
k,x,a,b = map(int, input().split())
b = min(b, k*x)
sums = {0}

for z in s:
    for nb in list(sums):
        sums.add(nb+z)

for t in range(b, a-1, -1):
    if t%x == 0 and t in sums:
        print(t)
        exit()

print("impossible")        