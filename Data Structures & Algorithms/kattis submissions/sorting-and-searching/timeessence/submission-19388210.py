s = input().split()
m = int(input())
vals = [int(s[i]) for i in range(2, len(s), 2)]
total1 = 1
total2 = 1

for i in range(len(vals)):
    total1 *= vals[i]
    
    if i > 0:
        total2 *= vals[i]

unit1 = m // total1
if 2*m >= total1 * (2*unit1+1):
    unit1 += 1

print(unit1, s[1])

A = m // total1
temp = m - A * total1
unit2 = temp // total2
remainder = temp % total2

if 2*remainder >= total2:
    unit2 += 1

if unit2 == vals[0]:
    A += 1
    unit2 = 0

print(A, s[1], unit2, s[3])