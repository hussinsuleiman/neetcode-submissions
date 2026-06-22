import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
CONST = 10 ** 9 + 7
nbBact = 2
isValid = True

for i in range(n):
    if b[i] > nbBact:
        print("error")
        isValid = False
        break
    
    nbBact -= b[i]
    nbBact *= 2

if isValid:
    print((nbBact // 2)%CONST)
    

