d1,d2,d3 = map(int, input().split())
n = int(input())

def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

l = lcm(lcm(d1,d2),d3)
vals = []

for i in range(1, l):
    if i%d1 != 0 and i%d2 != 0 and i%d3 != 0:
        vals.append(i)

t = len(vals)
res = l * ((n-1)//t) + vals[n%t-1]
print(res)