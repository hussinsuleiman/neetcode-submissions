def evalPoly(coeff, x, index):
    if index == len(coeff):
        return 0
    
    return coeff[index] + x * evalPoly(coeff, x, index+1)

nbs = list(map(int, input().split()))
n = nbs[0]
coeff = nbs[1:]
coeff.reverse()
pVal = [coeff[0]]

for i in range(1, n+1):
    pVal.append(evalPoly(coeff, i, 0))

C = [coeff[0]]
C.append(pVal[1] - pVal[0])

if n >= 2:
    C.append(pVal[2] - pVal[1] - C[-1])

if n >= 3:
    C.append(pVal[3] - pVal[2] - C[1] - 2 * C[2])

if n >= 4:
    C.append(pVal[4] - pVal[3] - C[1] - 3 * C[2] - 3 * C[3])

if n >= 5:
    C.append(pVal[5] - pVal[4] - C[1] - 4 * C[2] - 6 * C[3] - 4 * C[4])

if n >= 6:
    C.append(pVal[6] - pVal[5] - C[1] - 5 * C[2] - 10 * C[3] - 10 * C[4] - 5 * C[5])

for i in range(n+1):
    C[i] = str(C[i])

print(" ".join(C))
    
    

