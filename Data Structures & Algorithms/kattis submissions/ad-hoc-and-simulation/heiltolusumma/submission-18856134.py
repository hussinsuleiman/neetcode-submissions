N = int(input())

if N <= 0:
    print(1 + (-N)*(N-1) // 2)
else:
    print(N*(N+1) // 2)