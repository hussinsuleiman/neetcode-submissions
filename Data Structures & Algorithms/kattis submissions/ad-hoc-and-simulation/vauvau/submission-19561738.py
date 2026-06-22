A,B,C,D = map(int, input().split())
P,M,G = map(int, input().split())
P,M,G = P-1, M-1, G-1

p1,p2 = P%(A+B), P%(C+D)
nbG = 0

if p1 < A:
    nbG += 1

if p2 < C:
    nbG += 1

if nbG == 0:
    print('none')
elif nbG == 1:
    print('one')
else:
    print('both')

p1,p2 = M%(A+B), M%(C+D)
nbG = 0

if p1 < A:
    nbG += 1

if p2 < C:
    nbG += 1

if nbG == 0:
    print('none')
elif nbG == 1:
    print('one')
else:
    print('both')

p1,p2 = G%(A+B), G%(C+D)
nbG = 0

if p1 < A:
    nbG += 1

if p2 < C:
    nbG += 1

if nbG == 0:
    print('none')
elif nbG == 1:
    print('one')
else:
    print('both')