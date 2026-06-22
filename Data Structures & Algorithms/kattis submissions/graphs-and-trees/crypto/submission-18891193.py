N = int(input())
i = 2
total = 0
base = 2

while N >= i:
    cur = 0
    
    while N%i == 0:
        N //= i
        cur += 1
    
    if cur > total:
        total = cur
        base = i
    
    i += 1

print(base)
    

