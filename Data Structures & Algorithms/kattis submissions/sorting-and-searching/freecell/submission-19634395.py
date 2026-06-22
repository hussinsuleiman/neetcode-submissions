N,M,K = map(int, input().split())

if (N+1)*(2**M) >= K:
    print('yes')
else:
    print('no')