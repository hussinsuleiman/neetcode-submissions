import sys
input = sys.stdin.readline

s, v1, v2 = map(int, input().split())
start = s // v1 * v1
nbBottles = s // v1

while start >= 0 and (s - start) % v2 != 0:
    start -= v1
    nbBottles -= 1

if nbBottles < 0:
    print("Impossible")
else:
    print(nbBottles, (s - start) // v2)