n = int(input())
s = n

while n != 1:
    if n%2 == 1:
        n = n*3+1
    else:
        n //= 2
    
    s += n

print(s)