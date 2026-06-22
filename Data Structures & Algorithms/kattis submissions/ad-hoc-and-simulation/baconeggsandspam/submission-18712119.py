import sys
input = sys.stdin.readline

n = int(input())

while n != 0:
    dico = dict()
    
    for i in range(n):
        line = input().strip().split()
        name = line[0]
        
        for i in range(1, len(line)):
            if line[i] in dico.keys():
                dico[line[i]].append(name)
            else:
                dico[line[i]] = [name]
        
    items = sorted(dico.keys())
    
    for item in items:
        dico[item].sort()
        output = item + " " + " ".join(dico[item])
        print(output)
    
    print()
    n = int(input())
    
    
        