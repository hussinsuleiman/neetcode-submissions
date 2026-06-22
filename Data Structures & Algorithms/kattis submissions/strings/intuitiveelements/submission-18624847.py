import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a = set(input().strip())
    b = input().strip()
    isValid = True
    
    for letter in b:
        if isValid and letter not in a:
            print("NO")
            isValid = False
    
    if isValid:
        print("YES")
        
    
    