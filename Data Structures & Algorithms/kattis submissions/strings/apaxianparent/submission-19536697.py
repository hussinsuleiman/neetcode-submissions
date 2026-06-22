Y,P = input().split()

if Y[-1] == 'e':
    print(Y + 'x' + P)
elif Y[-1] in {'a', 'u', 'i', 'o'}:
    print(Y[:-1] + 'ex' + P)
elif (Y[-2], Y[-1]) == ('e', 'x'):
    print(Y + P)
else:
    print(Y + 'ex' + P)