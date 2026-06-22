B,G = map(int, input().split())

def fact(n):
    f = 1
    
    for i in range(1, n+1):
        f *= i
    
    return f

def C_n_k(n,k):
    return fact(n) // fact(k) // fact(n-k)

if min(B,G) == 0 or (B == G and B == 1):
    print(1)
    exit()

n = B+G
print((C_n_k(n, B) + n*C_n_k((n-1)//2, B//2))//(2*n))