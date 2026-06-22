n = int(input())
p = int(input())
S = set(map(int, input().split()))

for i in range(p, p+n):
    if i not in S:
        print(i)
        exit()