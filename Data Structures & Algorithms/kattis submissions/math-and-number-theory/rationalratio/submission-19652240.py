def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
        
    return a

f,n = input().split()
n = int(n)
I,F = f[:len(f)-n], f[-n:]
a,b = f.split('.')
exp = len(I) - len(a) - 1
i,k = I.split('.')
I,F = int(i)*(10**exp) + (int(k) if k else 0), int(F)

denom = (10**n-1)*(10**exp)
num = I*(10**n-1)+F
g = gcd(denom, num)
print(str(num//g) + '/' + str(denom//g))