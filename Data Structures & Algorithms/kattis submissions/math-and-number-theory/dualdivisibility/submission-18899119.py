def nbDiv(q):
    t = 0
    
    for i in range(1, int(q**0.5)):
        if q%i == 0:
            t += 2
    
    if q%(int(q**0.5)) == 0:
        if q**0.5 == int(q**0.5):
            t += 1
        else:
            t += 2
    
    return t

a,b = map(int, input().split())

if a%b != 0:
    print(0)
else:
    print(nbDiv(a//b))