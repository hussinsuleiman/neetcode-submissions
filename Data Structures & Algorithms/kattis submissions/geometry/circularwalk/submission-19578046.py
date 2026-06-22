n,b,k = map(int, input().split())

def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

g = gcd(n,k)

if b%g == 0:
    print('YES')
else:
    print('NO')