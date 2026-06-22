s,D = input().split()
D = int(D)
w = D

for i in range(len(s)):
    w += (2**i if s[i] == 'B' else 0)

output = []

while w > 0:
    if w%2 == 1:
        output.append("B")
    else:
        output.append('A')
    w //= 2

while len(output) < len(s):
    output.append('A')

print(''.join(output))