N = int(input())
s = 0

for i in range(N):
    g,b = map(int, input().split())
    s += g
    
    if s < b:
        print("impossible")
        exit()

print("possible")