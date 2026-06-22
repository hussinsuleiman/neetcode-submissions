n = int(input())
pas = []
perm = ['aA0!', 'aA!0', 'a0A!', 'a0!A', 'a!0A', 'a!A0', 'Aa0!', 'Aa!0', 'A0!a', 'A0a!']

for a in range(10):
    for b in range(10):
        for c in range(10):
            pas.append(perm[a] + perm[b] + perm[c])

for i in range(n):
    print(pas[i])

