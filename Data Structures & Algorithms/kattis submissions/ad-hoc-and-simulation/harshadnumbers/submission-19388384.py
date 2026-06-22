def isHarshad(n):
    s = 0
    k = n
    
    while n > 0:
        s += n%10
        n //= 10
    
    return k%s == 0

n = int(input())

while not isHarshad(n):
    n += 1

print(n)