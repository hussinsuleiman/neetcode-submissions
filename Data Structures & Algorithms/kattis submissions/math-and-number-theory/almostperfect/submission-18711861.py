import sys
import math

def divisors(n):
    d = set()
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    
    d.remove(n)
    return d

for n in sys.stdin:
    n = int(n)
    div = divisors(n)
    s = sum(div)
    
    if s == n:
        print(str(n) + " perfect")
    
    elif abs(s - n) <= 2:
        print(str(n) + " almost perfect")
    
    else:
        print(str(n) + " not perfect")
    
    