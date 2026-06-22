n = int(input())
nbFives = 0
nbZeroes = 0

for _ in range(n):
    d = int(input())
    
    if d%2 == 1 and d != 5:
        print(1)
        exit()
    
    if d == 5:
        nbFives += 1
    elif d == 0:
        nbZeroes += 1

if nbFives > 0 and nbFives + nbZeroes < n:
    print(1)
else:
    print(n)