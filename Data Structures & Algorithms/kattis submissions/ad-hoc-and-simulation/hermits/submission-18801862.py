import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
noise = a.copy()
M = int(input())

for i in range(M):
    x, y = map(int, input().split())
    noise[y-1] += a[x-1]
    noise[x-1] += a[y-1]

minStreet = 0

for i in range(1, N):
    if noise[minStreet] > noise[i]:
        minStreet = i

print(minStreet+1)