n = int(input())
res = 1
b = bin(n)[2:]
L = len(b)
ones = []

def fact(n):
    f = 1
    
    for i in range(1, n+1):
        f *= i
    
    return f

def C(n,k):
    return fact(n)//(fact(k)*fact(n-k))

for i in range(L):
    if b[i] == '1':
        ones.append(L-1-i)

for i in range(1, L):
    cnt = 0
    
    for j in ones:
        if cnt > i or i-cnt > j:
            break
        
        res += C(j,i-cnt)*(2**i)
        cnt += 1
    
print(res)