s = input()
l = len(s)
n = int(input())

for i in range(n):
    message = input()
    letters = []
    
    for i in range(l):
        letter = message[i]
        nb = ((ord(letter)-ord('A')) * int(s[i]))%26
        letters.append(chr(ord('A') + nb))
    
    print(''.join(letters))