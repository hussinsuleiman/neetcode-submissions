s = input()
res = []
i = 0
n = len(s)

while i < n:
    if s[i:i+8] == 'flatbaka':
        res.append('petsa')
        i += 8
    elif s[i:i+4] == 'bauk':
        res.append('dos')
        i += 4
    elif s[i] == 'k':
        res.append('g')
        i += 1
    elif s[i] == 'y':
        res.append('u')
        i += 1
    else:
        res.append(s[i])
        i += 1

print(''.join(res))