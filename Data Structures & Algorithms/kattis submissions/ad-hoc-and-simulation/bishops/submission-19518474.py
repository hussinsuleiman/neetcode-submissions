import sys

for line in sys.stdin:
    size = int(line)
    print(max(1,2*size-2))