import sys
import math
input = sys.stdin.readline

D, V = map(int, input().split())

while (D, V) != (0,0):
    print(((D**3 * math.pi - 6*V) / math.pi) ** (1/3))
    D, V = map(int, input().split())
