N = int(input())
a = list(map(int, input().split()))
print(max(2*max(a), sum(a)))