n = int(input())
nb = 1

while n != 0:
    strings = [input() for i in range(n)]
    res = [strings[i] for i in range(0, n, 2)]
    temp = n-1
    
    if n%2 == 1:
        temp -= 1
    
    for i in range(temp, 0, -2):
        res.append(strings[i])
    
    print("SET " + str(nb))
    print('\n'.join(res))
    nb += 1
    n = int(input())