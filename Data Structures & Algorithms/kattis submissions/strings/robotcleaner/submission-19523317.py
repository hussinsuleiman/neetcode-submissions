x,y = map(int, input().split())
x0,y0 = map(int, input().split())
n = int(input())
dirty = set([(i,i) for i in range(1, 1+min(x,y))])

for i in range(n):
    if not dirty:
        break
    
    k,d = input().split()
    k = int(k)
    
    if d == 'right':
        if x0 <= y0 and x0+k >= y0 and (y0,y0) in dirty:
            dirty.remove((y0,y0))
        x0 += k
    
    elif d == 'left':
        if x0 >= y0 and x0-k <= y0 and (y0,y0) in dirty:
            dirty.remove((y0,y0))
        x0 -= k
    
    elif d == 'up':
        if y0 <= x0 and y0+k >= x0 and (x0,x0) in dirty:
            dirty.remove((x0,x0))
        y0 += k
    
    elif d == 'down':
        if y0 >= x0 and y0-k <= x0 and (x0,x0) in dirty:
            dirty.remove((x0,x0))
        y0 -= k
    
    print(str(x0) + ' ' + str(y0))