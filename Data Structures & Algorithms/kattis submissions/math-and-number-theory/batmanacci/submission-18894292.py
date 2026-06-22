import sys
sys.setrecursionlimit(10**7)

N,K = map(int, input().split())
fib = [1,1]

for i in range(2,10**5+1):
    fib.append(fib[-1]+fib[-2])

def f(N,K):
    if N == 1:
        return "N"
    if N == 2:
        return "A"
    
    if K > fib[N-3]:
        return f(N-1,K-fib[N-3])
    
    return f(N-2,K)

print(f(N,K))