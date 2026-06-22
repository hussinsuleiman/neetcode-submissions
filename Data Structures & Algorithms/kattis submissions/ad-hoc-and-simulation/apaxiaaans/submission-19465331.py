s = input()
res = []

for i in range(len(s)):
    if res and res[-1] == s[i]:
        continue
    res.append(s[i])

print(''.join(res))