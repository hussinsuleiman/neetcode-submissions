import sys
input = sys.stdin.readline

while True:
    m = int(input())
    
    if m == 0:
        break
    
    w,h = 0,0
    curW, curH = 0, 0
    a,b = map(int, input().split())
        
    while (a,b) != (-1,-1):
        if curW + a <= m:
            curW += a
            curH = max(curH, b)
        
        else:
            w = max(w, curW)
            h += curH
            curW, curH = a, b
        
        a,b = map(int, input().split())
    
    w = max(curW, w)
    h += curH
    print(str(w) + ' x ' + str(h))