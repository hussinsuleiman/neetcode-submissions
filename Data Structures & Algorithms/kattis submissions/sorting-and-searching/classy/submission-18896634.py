import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    dico = dict()
    nbs = []
    
    for j in range(n):
        s = input().strip()
        name = []
        k = 0
        
        while s[k] != ':':
            name.append(s[k])
            k += 1
        
        k += 2
        nb = []
        
        while s[k] != ' ':
            if s[k] == '-':
                k += 1
                
            cur = []
            
            while s[k] != '-' and s[k] != ' ':
                cur.append(s[k])
                k += 1
            
            c = ''.join(cur)
            
            if c == 'upper':
                nb.append('0')
            elif c == 'lower':
                nb.append('2')
            else:
                nb.append('1')
        
        nb.reverse()
        
        while len(nb) < 10:
            nb.append('1')
        
        if ''.join(nb) in dico.keys():
            dico[''.join(nb)].append(''.join(name))
        else:
            dico[''.join(nb)] = [''.join(name)]
        
        dico[''.join(nb)].sort()            
        nbs.append(''.join(nb))
    
    nbs.sort()
    seen = set()
    
    for k in nbs:
        if k not in seen:
            seen.add(k)
            for elt in dico[k]:
                print(elt)
    
    line = ['='] * 30
    print(''.join(line))