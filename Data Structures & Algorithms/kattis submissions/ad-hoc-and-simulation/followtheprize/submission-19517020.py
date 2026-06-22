n = int(input())
pos = int(input())
m = int(input())

for i in range(m):
    a,b = map(int, input().split())
    
    if pos == b:
        pos = a
    elif pos == a:
        pos = b

print(pos)