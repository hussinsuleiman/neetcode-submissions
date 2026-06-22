n,V = map(int, input().split())
m = 0

for _ in range(n):
    l,w,h = map(int, input().split())
    m = max(m, l*w*h)

print(m-V)