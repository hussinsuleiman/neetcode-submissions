def gcd(a,b):
    while b != 0:
        temp = a%b
        a,b = b,temp
    return a

inp = input()
i,f = inp.split('.')
P = float(inp)
den = 10**len(f)
num = P*den
num = int(num)
g = gcd(num, den)
num //= g
den //= g
res = [0]*5

if P <= 2:
    res[1] = num-den
    res[0] = den-res[1]
    
elif P <= 3:
    res[2] = num-2*den
    res[1] = den-res[2]
    
elif P <= 4:
    res[3] = num-3*den
    res[2] = den-res[3]
    
else:
    res[4] = num-4*den
    res[3] = den-res[4]

res = [str(res[i]) for i in range(5)]
print(' '.join(res))