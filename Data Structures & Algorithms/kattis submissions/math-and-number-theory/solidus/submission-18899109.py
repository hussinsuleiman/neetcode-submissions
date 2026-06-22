def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

a = int(input())
line = input()
b = int(input())

if a%b == 0:
    print(a//b)
else:
    u,v = max(abs(a),abs(b)), min(abs(a),abs(b))
    a,b = a//gcd(u,v), b//gcd(u,v)
    
    if b < 0:
        a,b = -a,-b
            
    print(str(a) + '/' + str(b))