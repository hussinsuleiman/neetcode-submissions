from math import log

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    exp = 1
    s = a+b+1
    i = 0
    
    while s > exp:
        exp *= 2 
        i += 1
    
    if s == exp:
        print(i)
    else:
        print(-1)