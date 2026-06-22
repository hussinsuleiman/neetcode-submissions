import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dico = dict()

for i in range(n):
    dico[a[i]] = i+1 

a.sort()
highest = []
i = 0

while i < n:
    if not highest or a[i] > highest[-1]:
        highest.append(a[i])
        i += 1
    else:
        while i < n and highest[-1] == a[i]:
            i += 1
        highest.pop()

if not highest:
    print("none")
else:
    print(dico[highest[-1]])