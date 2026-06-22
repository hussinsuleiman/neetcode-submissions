n = int(input())
nbs = list(map(int, input().split()))
cnt = 0
s = 0

for k in nbs:
    if k >= 0:
        cnt += 1
        s += k

print(float(s)/cnt)