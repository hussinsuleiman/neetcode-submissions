import sys

for line in sys.stdin:
    nbs = map(int, line.split())
    print(sum(nbs) // 2)
