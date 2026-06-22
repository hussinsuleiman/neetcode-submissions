N,K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a[(N-K+1)//2])