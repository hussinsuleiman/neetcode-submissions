import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
i, j = 0, n-1
nbTrips = 0

while i <= j:
    if w[i] + w[j] > m:
        j -= 1
    else:
        i += 1
        j -= 1
    nbTrips += 1

print(nbTrips)

