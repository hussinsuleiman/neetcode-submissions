import sys

for line in sys.stdin:
    a,b,c = map(int, line.split())
    res = ['0.']
    a *= 10
    
    for i in range(c):
        res.append(str(a//b))
        a = (a%b)*10
    
    print(''.join(res))