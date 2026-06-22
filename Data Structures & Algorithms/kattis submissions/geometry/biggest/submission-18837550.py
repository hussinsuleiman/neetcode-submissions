import sys
import math
input = sys.stdin.readline

m = int(input())

for i in range(m):
    r, n, thetaDeg, thetaMin, thetaSec = map(int, input().split())
    cuts = [0.0]
    rotAngle = thetaDeg + thetaMin / 60 + thetaSec / 3600
    angle = 0
    visited = set()
    oneTurn = (n-1) * rotAngle < 360
    
    for j in range(n-1):
        angle = (angle + rotAngle) % 360
        
        if angle in visited:
            break
        
        visited.add(angle)
        cuts.append(angle)
        
    cuts.sort()
    maxDiff = 0
    
    for j in range(len(cuts)-1):
        if cuts[j+1] - cuts[j] > maxDiff:
            maxDiff = cuts[j+1] - cuts[j]
    
    if oneTurn and 360 - cuts[-1] > maxDiff:
        maxDiff = 360 - cuts[-1]
    
    print(maxDiff / 360 * r**2 * math.pi)