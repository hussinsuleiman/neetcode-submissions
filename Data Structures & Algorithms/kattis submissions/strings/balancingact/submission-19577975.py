n = int(input())
s = input()

if n%2 == 1:
    print('NO')
    exit()

diff = set([0])

for i in range(n):
    new = set()
    
    for d in diff:
        if s[i] == '(':
            new.add(d+1)
    
        elif s[i] == ')':
            if d > 0:
                new.add(d-1)
    
        elif d > 0:
            new.add(d-1)
            new.add(d+1)
        
        else:
            new.add(d+1)
    
    diff = new

if 0 in diff:
    print('YES')
else:
    print('NO')