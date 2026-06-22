import sys
input = sys.stdin.readline

n = int(input())

while n != 0:
    nbs1 = []
    nbs2 = []
    
    for i in range(n):
        nbs1.append(int(input()))
    for i in range(n):
        nbs2.append(int(input()))
        
    sorted1 = nbs1.copy()
    sorted2 = nbs2.copy()
    sorted1.sort()
    sorted2.sort()
    matches = dict()
    
    for i in range(n):
        matches[sorted1[i]] = sorted2[i]
    
    output = []
    
    for i in range(n):
        output.append(str(matches[nbs1[i]]))
    
    print("\n".join(output))    
    
    n = int(input())
    if n != 0:
        print()