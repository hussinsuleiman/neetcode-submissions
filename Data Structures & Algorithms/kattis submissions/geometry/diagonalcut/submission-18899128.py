def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

M,N = map(int, input().split())
g = gcd(M,N)
M,N = M//g, N//g

if (M-N)%2 != 0:
    print(0)
else:
    print(g)