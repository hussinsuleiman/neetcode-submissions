N = int(input())
s = 0
t = 0

for i in range(N):
    a = int(input())

    if a > 0:
        t += 1
        s += a

print(s+1-t)