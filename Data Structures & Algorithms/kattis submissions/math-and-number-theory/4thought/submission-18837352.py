import sys
input = sys.stdin.readline

def evalExp(nbs, ops):
    index = 0
    
    while index < len(ops):
        if ops[index] == '+':
            nbs[index+1] += nbs[index]
        else:
            nbs[index+1] = nbs[index] - nbs[index+1]
        
        index += 1
    
    return nbs[-1]

op = ['+', '-', '/', '*']
dico = dict()

for i in range(4):
    for j in range(4):
        for k in range(4):
            nbs = [4]
            ops = []
                
            if i == 0 or i == 1:
                nbs = [4, 4]
                
                if i == 0:
                    ops.append('+')
                else:
                    ops.append('-')
            elif i == 2:
                nbs = [1]
            else:
                nbs = [16]
                
            if j == 0 or j == 1:
                nbs.append(4)
                
                if j == 0:
                    ops.append('+')
                else:
                    ops.append('-')    
            elif j == 2:
                nbs[-1] //= 4
            else:
                nbs[-1] *= 4
             
            if k == 0 or k == 1:
                nbs.append(4)
                
                if k == 0:
                    ops.append('+')
                else:
                    ops.append('-')
            elif k == 2:
                nbs[-1] //= 4
            else:
                nbs[-1] *= 4
                    
            value = evalExp(nbs, ops)
            dico[value] = '4 ' + op[i] + ' 4 ' + op[j] + ' 4 ' + op[k] + ' 4 = ' + str(value)

m = int(input())

for i in range(m):
    n = int(input())
    
    if n in dico.keys():
        print(dico[n])
    else:
        print("no solution")