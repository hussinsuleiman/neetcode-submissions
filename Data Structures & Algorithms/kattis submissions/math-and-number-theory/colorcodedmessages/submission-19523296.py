n = int(input())
colors = {(255,255,255): 'w', (0,0,255): 'b', (255,0,255): 'f', (255,165,0): 'o', (18,10,143): "u", (220,20,60): 'c', (255,0,0): 'r', (255,255,0): 'y', (192,192,192): 's', (75,0,130): 'i', (165,42,42): 'h', (0,255,0): 'g', (0,255,255): 'a', (128,0,0): 'm', (80,200,120): 'e', (255,192,203): 'p', (0,0,0): ' '}
RGB = list(colors.keys())
ans = []

for i in range(n):
    r,g,b = map(int, input().split())
    m = r+g+b
    best = (0,0,0)
    
    for R,G,B in RGB:
        if abs(R-r) + abs(G-g) + abs(B-b) < abs(best[0]-r) + abs(best[1]-g) + abs(best[2]-b):
            best = (R,G,B)
    
    ans.append(colors[best])

print(''.join(ans))