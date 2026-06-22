import sys
input = sys.stdin.readline

d, N = input().split()
d, N = float(d), int(N)

while (d, N) != (0.0, 0):
    beehives = []
    sour = set()
    
    for i in range(N):
        x, y = map(float, input().split())
        beehives.append((x, y))
    
    for i in range(N):
        x1, y1 = beehives[i]
        
        for j in range(i+1, N):
            x2, y2 = beehives[j]
            
            if (x2-x1) ** 2 + (y2-y1) ** 2 <= d ** 2:
                sour.add(i)
                sour.add(j)
    
    l = len(sour)
    print(str(l) + " sour, " + str(N - l) + " sweet")
    
    d, N = input().split()
    d, N = float(d), int(N) 