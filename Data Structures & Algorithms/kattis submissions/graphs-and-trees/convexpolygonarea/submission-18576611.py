def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0  

    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n] 
        area += (x1 * y2) - (x2 * y1)

    return abs(area / 2.0)

n = int(input())

for i in range(n):
    nbs = list(map(int, input().split()))
    k = nbs[0]
    vertices = []
    
    for i in range(1, 2*k+1, 2):
        vertices.append((nbs[i], nbs[i+1]))
    
    print(polygon_area(vertices))
    