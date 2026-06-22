N = input()
l = len(N)
digits = [N[i] for i in range(l)]
nbs = [int(N[i]) for i in range(l)]
s = sum(nbs)-1
res = ['0'] * (l+1)
res[0] = '1'
i = l

while s >= 9:
    res[i] = '9'
    s -= 9
    i -= 1

res[i] = str(s)
left, right = -1,-1

for i in range(l-1, -1, -1):
    if digits[i] != '0':
        right = i
        break
    
for i in range(right-1, -1, -1):
    if digits[i] != '9':
        left = i
        break

if left == -1:
    print(''.join(res))
else:
    digits[left] = str(int(digits[left])+1)
    s = -1
    
    for k in range(left+1, l):
        s += nbs[k]

    i = l-1

    while s >= 9:
        digits[i] = '9'
        s -= 9
        i -= 1

    digits[i] = str(s)
    
    for k in range(i-1, left, -1):
        digits[k] = '0'
    
    print(''.join(digits))