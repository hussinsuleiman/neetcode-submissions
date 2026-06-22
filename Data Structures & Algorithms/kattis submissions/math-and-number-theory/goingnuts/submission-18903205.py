n = int(input())
s = bin(n)
t = 0

for i in s:
    if i == '1':
        t += 1

print(t)
