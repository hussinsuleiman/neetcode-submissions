import sys
input = sys.stdin.readline

N = int(input())
s = input()
hasLorV = False
foundLV = False

for i in range(N):
    if s[i] == 'l':
        if i < N-1 and s[i+1] == 'v':
            print(0)
            foundLV = True
            break
        hasLorV = True
    
    elif s[i] == 'v':
        hasLorV = True
    
if not foundLV:
    if hasLorV:
        print(1)
    else:
        print(2)