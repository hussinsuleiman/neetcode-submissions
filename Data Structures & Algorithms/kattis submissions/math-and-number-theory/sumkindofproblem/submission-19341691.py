P = int(input())

for i in range(P):
    K,N = map(int, input().split())
    s = N*(N+1) // 2
    print(str(K) + ' ' + str(s) + ' ' + str(N**2) + ' ' + str(2*s))