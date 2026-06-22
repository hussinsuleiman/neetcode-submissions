x1, x2 = map(int, input().split())
a,b = map(int, input().split())
c,d = map(int, input().split())
q = int(input())
MOD = 10**9+7

nbs = [x1, x2]

for i in range(3, 10**5+1):
    if i%2 == 1:
        nbs.append((c*nbs[-1] + d*nbs[-2])%MOD)
    else:
        nbs.append((a*nbs[-1] + b*i)%MOD)

for _ in range(q):
    k = int(input())
    print(nbs[k-1])