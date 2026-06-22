import sys
import math
input = sys.stdin.readline

def divisors(k):
    div = [k]
    
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            div.append(i)
            div.append(k // i)
            
    return div

def isPrime(k):
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

n = int(input())

while n != 0:
    result = n
    d = divisors(n)
    
    for div in d:
        if isPrime(div):
            result *= (1-1/div)
    
    print(int(result))
    n = int(input())