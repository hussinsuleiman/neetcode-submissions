n = int(input())

def lcm(x,y):
    p = x*y
    
    while y != 0:
        temp = x%y
        x = y
        y = temp
    
    return p//x

while n != 0:
    step = 1
    up = float('inf')
    down = 0
    
    for i in range(n):
        clue = input().split()
        k = int(clue[2])
        
        if clue[0] == 'less':
            up = min(up, k)
        
        elif clue[0] == 'greater':
            down = max(down, k)
        
        else:
            step = lcm(step, k)
    
    if up == float('inf'):
        print('infinite')
    else:
        vals = []
            
        for i in range(down+1, up):
            if i%step == 0:
                vals.append(str(i))
        
        if not vals:
            print("none")
        else:
            print(" ".join(vals))
        
    n = int(input())