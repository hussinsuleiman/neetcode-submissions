def egcd(a, b):
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def inv_mod(a, mod):
    g, x, _ = egcd(a, mod)
    return x % mod

def crt_coprime(a, n, b, m):
    a %= n
    b %= m
    inv_n = inv_mod(n % m, m)            
    t = ((b - a) % m) * inv_n % m
    x = a + n * t
    mod = n * m
    return str(x % mod) + ' ' + str(mod)

T = int(input())

for i in range(T):
    a,n,b,m = map(int, input().split())
    print(crt_coprime(a,n,b,m))