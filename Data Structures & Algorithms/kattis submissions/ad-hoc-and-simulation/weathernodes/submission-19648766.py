N = int(input())

if N == 0:
    print(0)
    exit()

temp = [float(input()) for i in range(N)]
a = sum(temp)/N
res = 0

for t in temp:
    if abs(a-t) > 10:
        res += 1

print(res)