T = int(input())

for i in range(T):
    k = int(input())
    a = 1
    
    while 2**(a+1) <= k+1:
        a += 1
    
    nb = ['0'] * a
    rest = k-2**a+1
    exp = a-1
    
    while rest > 0:
        if rest%2 == 1:
            nb[exp] = '1'
            
        rest //= 2
        exp -= 1
    
    print(''.join(nb))
    
    
    