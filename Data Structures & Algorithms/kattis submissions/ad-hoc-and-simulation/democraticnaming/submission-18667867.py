import sys
input = sys.stdin.readline

n,m = map(int, input().split())
output = []
cities = []

for i in range(n):
    cities.append(input().strip())

for i in range(m):
    dico = dict()
    
    for j in range(n):
        if cities[j][i] in dico.keys():
            dico[cities[j][i]] += 1
        else:
            dico[cities[j][i]] = 1
    
    maxVal = max(dico.values())
    possible = []
    
    for elt in dico.keys():
        if dico[elt] == maxVal:
            possible.append(elt)
    
    possible.sort()
    output.append(possible[0])

print("".join(output))