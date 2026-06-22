n = int(input())
d = list(map(int, input().split()))
d.sort()
print(sum(d)-d[0]+d[-1])