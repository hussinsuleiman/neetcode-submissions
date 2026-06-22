W,S,C,K = map(int, input().split())

if S > K and W+C > K:
    print('NO')
elif min(S, W+C) < K:
    print('YES')
elif S <= K:
    print('YES' if W+C <= 2*K else 'NO')
else:
    print('YES' if S <= 2*K else 'NO')