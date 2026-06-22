s = input().split('/')
mult = []
parts = []

for elt in s:
    new = elt.split('*')
    
    for i in range(len(new)-1):
        mult.append('*')
    
    mult.append('/')
    parts += new
    
res = []

for p in parts:
    res.append(eval(p))

cur = float(res[0])

for i in range(len(mult)-1):
    if mult[i] == '*':
        cur *= res[i+1]
    else:
        cur /= res[i+1]

print(int(cur))