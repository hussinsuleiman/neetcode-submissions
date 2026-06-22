n = int(input())
s = 0
fact = [1]

for i in range(1, 10001):
    fact.append(fact[-1]*i)

def c(k):
    return fact[2*k]//((fact[k])**2 * (k+1))
    
for k in range((n+1)//2):
    s += c(k)*c(n-k)

s *= 2
print(s if n%2 == 1 else s+c(n//2)**2)