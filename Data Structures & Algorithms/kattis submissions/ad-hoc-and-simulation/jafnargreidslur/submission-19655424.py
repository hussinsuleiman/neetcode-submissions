x,n,q = map(int, input().split())
p = q/10000
print(x*p/(1-pow(1+p,-n)))