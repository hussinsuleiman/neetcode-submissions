import sys
input = sys.stdin.readline

R, B = map(int, input().split())
delta = (((R+4) / 2) ** 2 - 4*(B+R)) ** 0.5
W = int(((R+4) / 2 - delta) / 2)
L = int(((R+4) / 2 + delta) / 2)
print(L, W)