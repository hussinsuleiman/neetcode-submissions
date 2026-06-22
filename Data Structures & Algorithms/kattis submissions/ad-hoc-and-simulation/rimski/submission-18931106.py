s = input()
l = len(s)
res = [s[i] for i in range(l)]

if (l >= 2) and (s[0] == 'L' and s[1] == 'X' and (l == 2 or s[2] != 'X' or s == 'LXXI')):
    res[0], res[1] = res[1], res[0]

if l >= 2 and res[-2] in {'V', 'X'} and res[-1] == 'I':
    res[-2], res[-1] = res[-1], res[-2]

print(''.join(res))