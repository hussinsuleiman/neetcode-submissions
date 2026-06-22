import sys
m = {'0':'0', '1':'1', '2':'2', '3':'5', '4':'9', '5':'8', '6':'6'}

def to_base7(n):
    return "" if n == 0 else to_base7(n // 7) + str(n % 7)

for k in sys.stdin:
    s = to_base7(int(k))
    res = []
    
    for i in range(len(s)-1,-1,-1):
        res.append(m[s[i]])
    
    print(''.join(res))