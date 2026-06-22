import sys
input = sys.stdin.readline

nbs = list(map(int, input().split()))
towerA = nbs[6]
towerB = nbs[7]
boxesA = []
boxesB = []

for i in range(0, 4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            if nbs[i] + nbs[j] + nbs[k] == towerA:
                boxesA = [nbs[i], nbs[j], nbs[k]]
                boxesA.sort()
                break

for i in range(0, 6):
    if nbs[i] not in boxesA:
        boxesB.append(nbs[i])

boxesB.sort()
output = ""

for i in range(2, -1, -1):
    output += str(boxesA[i]) + " "

for j in range(2, 0, -1):
    output += str(boxesB[j]) + " "
    
output += str(boxesB[0])
print(output)