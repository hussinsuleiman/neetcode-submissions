s = input()
seen = set()

for c in s:
    seen.add(ord(c)-ord('A'))

ans = []

for i in range(26):
    if i not in seen:
        ans.append(chr(ord('A')+i))

if ans:
    print(''.join(ans))
else:
    print("Alphabet Soup!")