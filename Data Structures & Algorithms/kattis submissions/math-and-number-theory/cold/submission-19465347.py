n = int(input())
temps = list(map(int, input().split()))
res = 0

for t in temps:
    if t < 0:
        res += 1

print(res)