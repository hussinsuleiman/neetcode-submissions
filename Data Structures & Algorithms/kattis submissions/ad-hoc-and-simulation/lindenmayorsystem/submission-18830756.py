n, m = map(int, input().split())
rules = dict()

for i in range(n):
    line = input().split()
    rules[line[0]] = line[2]

S = input()

for i in range(m):
    newS = []
    
    for j in range(len(S)):
        if S[j] not in rules.keys():
            newS.append(S[j])
        else:
            newS.append(rules[S[j]])
    
    S = ''.join(newS)

print(S)