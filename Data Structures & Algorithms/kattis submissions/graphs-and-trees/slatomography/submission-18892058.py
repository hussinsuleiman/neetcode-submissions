N = int(input())
total = 1
prev = 0

for i in range(N):
    cur = int(input())
    if cur > prev:
        total += cur-prev+1
    prev = cur

print(total)