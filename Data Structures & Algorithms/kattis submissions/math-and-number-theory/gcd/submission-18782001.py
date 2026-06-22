a,b = map(int, input().split())

if a < b:
    a,b = b,a

while b > 0:
    temp = a % b
    a = b
    b = temp

print(a)