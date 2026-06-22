import sys
input = sys.stdin.readline

a, b = map(int, input().split())

while (a,b) != (0,0):
    print(str(a // b) + ' ' + str(a % b) + ' / ' + str(b))
    a, b = map(int, input().split())
