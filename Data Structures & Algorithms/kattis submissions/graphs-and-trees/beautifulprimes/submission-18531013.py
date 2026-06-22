import sys
input = sys.stdin.readline


T = int(input())
nbs = []
prod = 1

for i in range(1000):
    if prod * 5 >= 10 ** i:
        nbs.append('5')
        prod *= 5
    else:
        nbs.append('11')
        prod *= 11
        
for i in range(T):
    N = int(input())
    print(" ".join(nbs[:N]))
    