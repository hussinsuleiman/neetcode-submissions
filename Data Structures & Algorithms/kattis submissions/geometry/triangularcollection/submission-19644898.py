n = int(input())
nbs = [int(input()) for i in range(n)]
nbs.sort()
res = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nbs[k] < nbs[i] + nbs[j]:
                res += 2**(k-j-1)

print(res)