n = int(input())
r = list(map(int, input().split()))
i = 0

for j in range(1, n):
    if r[j] > r[i]:
        i = j

print(str(i) + ' ' + str(i))