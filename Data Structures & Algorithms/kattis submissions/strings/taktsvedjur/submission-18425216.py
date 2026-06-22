import sys
input = sys.stdin.readline

n = int(input())
mult = 1
total = 0
cons = 0

for i in range(n):
    nb = int(input())
    
    if nb == 0:
        if mult > 1:
            mult //= 2
        cons = 0
    
    elif nb > 0:
        cons += 1
        
        if cons // 2 == mult and mult < 8:
            mult *= 2
            cons = 0
        
        total += nb * mult

print(total)
            