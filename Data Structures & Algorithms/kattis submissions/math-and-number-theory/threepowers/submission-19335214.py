n = int(input())

while n != 0:
    s = bin(n-1)
    l = len(s)
    res = []
    
    for i in range(2, l):
        if s[i] == '1':
            res.append(str(3**(l-i-1)))
            
    res.reverse()    
    res = ', '.join(res)
    print("{ " + res + " }")
    n = int(input())