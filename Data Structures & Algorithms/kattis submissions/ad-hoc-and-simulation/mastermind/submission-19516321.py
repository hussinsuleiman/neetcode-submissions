n,code,guess = input().split()
n = int(n)
cntCode = [0] * 26

for c in code:
    cntCode[ord(c)-ord('A')] += 1

r,s = 0,0
match = set()

for i in range(n):
    if code[i] == guess[i]:
        r += 1
        match.add(i)
        cntCode[ord(guess[i])-ord('A')] -= 1

for i in range(n):
    if i in match:
        continue
    
    if cntCode[ord(guess[i])-ord('A')] > 0:
        cntCode[ord(guess[i])-ord('A')] -= 1
        s += 1

print(str(r) + ' ' + str(s))