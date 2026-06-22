import sys
input = sys.stdin.readline

n, p = map(int, input().split())
properties = [[] for i in range(p)]
possible = []
result = 0

for i in range(n):
    c = list(map(int, input().split()))
    
    for j in range(p):
        properties[j].append(c[j])

for j in range(p):
    dico = dict()
    
    for i in range(n):
        dico[properties[j][i]] = i
    
    properties[j].sort()
    valid = True
    order = [dico[properties[j][0]]]
    
    for i in range(1, n):
        if properties[j][i] == properties[j][i-1]:
            valid = False
            break
        else:
            order.append(dico[properties[j][i]])
            
    if valid:
        for j in range(len(possible)):
            if not valid:
                break
            
            for i in range(n):
                if possible[j][i] != order[i]:
                    break
                if i == n-1:
                    valid = False
                    break
                    
    if valid:
        result += 1
        possible.append(order)

print(result)




