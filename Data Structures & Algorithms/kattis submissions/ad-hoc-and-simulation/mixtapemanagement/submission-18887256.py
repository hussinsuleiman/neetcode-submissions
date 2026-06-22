n = int(input())
nbs = list(map(int, input().split()))
res = []

for i in range(n):
    a = str((10**nbs[i]-1)//9)
    if i < 10:
        res.append("10" + str(i) + a)
    else:
        res.append("1" + str(i) + a)

print(' '.join(res))