import sys
input = sys.stdin.readline

R, C = map(int, input().split())

if R*C % 2 == 0:
    print("Alf")
else:
    print("Beata")
