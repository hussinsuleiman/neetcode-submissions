n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

a.sort()
i = 0

while i < n and i < a[n-1-i]:
    i += 1

print(i)