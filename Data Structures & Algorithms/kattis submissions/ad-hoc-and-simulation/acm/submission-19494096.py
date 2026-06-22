from collections import defaultdict

line = input()
d = defaultdict(int)
total = 0
nbSolved = 0

while line != '-1':
    m, problem, solve = line.split()
    m = int(m)
    
    if solve == 'right':
        total += m + 20*d[problem]
        nbSolved += 1
    else:
        d[problem] += 1
    
    line = input()

print(str(nbSolved) + ' ' + str(total))