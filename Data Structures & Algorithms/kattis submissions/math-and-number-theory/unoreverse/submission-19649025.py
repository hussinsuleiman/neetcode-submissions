K,N = map(int, input().split())

if N == 0:
    print('NO')
elif N == 1 or K == 2:
    print('YES')
elif N%2 == 1:
    print('MAYBE')
elif N >= 2*K-2:
    print('MAYBE')
else:
    print("NO")