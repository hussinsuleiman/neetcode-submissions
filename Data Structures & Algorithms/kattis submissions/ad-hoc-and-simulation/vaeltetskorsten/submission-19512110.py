n = int(input())
m = 0

for _ in range(n):
    i,s = input().split()
    i = int(i)
    
    if s == 'nej':
        m = max(m,i)

print(m)