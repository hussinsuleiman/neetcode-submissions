n = int(input())
dirs = input().split()
cntN = 0

for d in dirs:
    if d == 'N':
        cntN += 1

cnt = min(cntN, n - cntN)
res = 1
f = 1

for i in range(n, n-cnt, -1):
    res *= i
    f *= (n+1-i)

print(res//f-1)