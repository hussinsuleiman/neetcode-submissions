T,R = map(int, input().split())
towers = []
pts = []

for i in range(T):
    x,y,p = map(int, input().split())
    towers.append((x,y,p))

line = list(map(int, input().split()))
zero = input()
pts = []

for i in range(R+1):
    x,y = line[2*i], line[2*i+1]
    pts.append((x,y))

dist = 0
mile = 0
markers = []

for i in range(R):
    x2, y2 = pts[i+1] 
    x1, y1 = pts[i]
    cur = ((x2-x1) ** 2 + (y2-y1) ** 2) ** (0.5)
    
    while dist + cur >= mile:
        C = (mile-dist) / cur
        x,y = x1 + C * (x2-x1), y1 + C * (y2-y1) 
        strengthMax = 0
        towerMax = ''
        letter = 'A'
        
        for t1, t2, p in towers:
            d_sq = (t1-x) ** 2 + (t2-y) ** 2
            strength = float(p) / d_sq
            
            if strength - int(strength) >= 0.5:
                strength = int(strength) + 1
            else:
                strength = int(strength)
            
            if strength > strengthMax:
                strengthMax = strength
                towerMax = letter
            
            letter = chr(ord(letter)+1)
        
        if not markers or markers[-1][-2] != towerMax:
            markers.append('(' + str(mile) + ',' + towerMax + ')')
            
        mile += 1
    
    dist += cur

if dist - int(dist) >= 0.5:
    x,y = pts[-1]
    strengthMax = 0
    towerMax = ''
    letter = 'A'
    
    for t1, t2, p in towers:
        d_sq = (t1-x) ** 2 + (t2-y) ** 2
        strength = float(p) / d_sq
        
        if strength - int(strength) >= 0.5:
            strength = int(strength) + 1
        else:
            strength = int(strength)
        
        if strength > strengthMax:
            strengthMax = strength
            towerMax = letter
        
        letter = chr(ord(letter)+1)
    
    if not markers or markers[-1][-2] != towerMax:
        markers.append('(' + str(mile) + ',' + towerMax + ')')

print(' '.join(markers))