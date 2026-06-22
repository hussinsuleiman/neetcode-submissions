n,k = map(int, input().split())
s = 0

for _ in range(k):
    s += int(input())

m = s - (n-k)*3
M = s + (n-k)*3
print(str(m/n) + ' ' + str(M/n))