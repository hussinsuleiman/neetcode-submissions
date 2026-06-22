n,s = input().split()
n = int(n)

if s == 'out':
    n -= 1

if n <= 1:
    print(1)
    exit()

n -= n%2
res = 1
pos = 2

while pos != 1:
    if pos > n//2:
        pos = (pos*2-1)%n
    else:
        pos = (pos*2)%n
    
    if pos == 0:
        pos = n
    
    res += 1

print(res)