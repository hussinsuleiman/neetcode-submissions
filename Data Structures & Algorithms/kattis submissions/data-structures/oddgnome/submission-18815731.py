import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    nbs = list(map(int, input().split()))
    j = 1
    
    while nbs[j+1] - nbs[j] == 1:
        j += 1
    
    print(j+1)
    