N = int(input())
pts = []

for i in range(N):
    X, Y = map(float, input().split())
    pts.append((X, Y))

curArea = 0

for i in range(N-1):
    curArea += pts[i][0] * pts[i+1][1] - pts[i][1] * pts[i+1][0]

curArea += pts[N-1][0] * pts[0][1] - pts[N-1][1] * pts[0][0]
curArea /= 2
A = int(input())
ratio = (A / curArea) ** 0.5
minX, minY = 500, 500

for i in range(N):
    pts[i] = (pts[i][0] * ratio, pts[i][1] * ratio)
    
    if pts[i][0] < minX:
        minX = pts[i][0]
    if pts[i][1] < minY:
        minY = pts[i][1]

for i in range(N):
    print(pts[i][0] - minX, pts[i][1] - minY)

