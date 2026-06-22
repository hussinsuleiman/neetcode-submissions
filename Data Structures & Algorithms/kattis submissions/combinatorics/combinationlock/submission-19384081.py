import sys

for line in sys.stdin:
    a,b,c,d = map(int, line.split())
    
    if (a,b,c,d) == (0,0,0,0):
        exit()
    
    res = 3*360 + 9*((a-b)%40) + 9*((c-b)%40) + 9*((c-d)%40)
    print(res)