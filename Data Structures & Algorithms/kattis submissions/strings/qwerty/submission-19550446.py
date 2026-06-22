N = int(input())
s = input()
ans = []
qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

for c in s:
    if c == ' ':
        ans.append(' ')
    else:
        ans.append(qwerty[ord(c)-ord('a')])

print(''.join(ans))