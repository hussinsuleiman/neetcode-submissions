import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))

occ = defaultdict(int)
sumPrices = 0
totInf = 0

for price in p:
    occ[price] += 1
    sumPrices += price

Q = int(input())

for i in range(Q):
    command = list(map(str, input().split()))
    
    if len(command) == 2:
        currInf = int(command[1])
        totInf += currInf
        sumPrices += currInf * N
    
    else:
        x, y = int(command[1]), int(command[2])
        o = occ[x-totInf]
        occ[x-totInf] = 0
        occ[y-totInf] += o
        sumPrices += (y-x)*o
    
    print(sumPrices)
