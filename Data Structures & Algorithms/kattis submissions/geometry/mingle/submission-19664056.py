n,k = map(int, input().split())
a = (2*k)**(2*k)*n
b = (2*k+1)**(2*k)
MOD = 998244353
print((a*pow(b, -1, MOD))%MOD)