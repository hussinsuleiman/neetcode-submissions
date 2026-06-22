s = input()
nbWhite, nbBlack = 0, 0

for c in s:
    if c == 'W':
        nbWhite += 1
    else:
        nbBlack += 1

if nbWhite == nbBlack:
    print(1)
else:
    print(0)