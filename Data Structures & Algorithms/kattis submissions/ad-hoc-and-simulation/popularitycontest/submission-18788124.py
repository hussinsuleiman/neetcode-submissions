import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nbFriends = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    nbFriends[a-1] += 1
    nbFriends[b-1] += 1

for i in range(N):
    nbFriends[i] = str(nbFriends[i]-i-1)

print(" ".join(nbFriends))