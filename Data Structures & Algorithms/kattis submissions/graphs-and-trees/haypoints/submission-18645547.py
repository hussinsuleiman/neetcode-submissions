import sys
input = sys.stdin.readline

m, n = map(int, input().split())
dico = dict()

for i in range(m):
    s, d = input().strip().split()
    d = int(d)
    dico[s] = d

for i in range(n):
    line = input().strip()
    total = 0
    
    while line != '.':
        line = line.split()
        
        for word in line:
            if word in dico.keys():
                total += dico[word]
        
        line = input().strip()
    
    print(total)