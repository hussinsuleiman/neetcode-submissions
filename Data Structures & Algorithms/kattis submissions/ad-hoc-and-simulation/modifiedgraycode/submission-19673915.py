N = int(input())

for _ in range(N):
    K = int(input())
    b = bin(K)[2:]
    nb = 0
    
    for c in b:
        if c == '1':
            nb += 1
    
    if nb%2 == 1:
        b += '1'
    else:
        b += '0'
    
    l = len(b)
    
    for k in range(10-l):
        b = '0' + b
    
    print(b)