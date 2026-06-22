t = int(input())
h = 0

while (t + 300*h)%55 != 0:
    h += 1

m = (t + 300*h)//55
h += m//60
m %= 60

H = str(h)
M = str(m)

if h < 10:
    H = '0' + H
    
if m < 10:
    M = '0' + M

print(H + ':' + M)