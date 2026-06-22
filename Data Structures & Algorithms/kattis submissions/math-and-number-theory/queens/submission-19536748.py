N = int(input())
pos = []

for _ in range(N):
    x,y = map(int, input().split())
    
    for a,b in pos:
        if x == a or y == b or (x-a) == (y-b) or (x-a) == (b-y):
            print("INCORRECT")
            exit()
    
    pos.append((x,y))

print("CORRECT")    