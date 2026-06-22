a,b = map(int, input().split())
tot = 0

while a > b:
    tot += a%2 + 1
    a = (a + a%2)//2

print(tot+b-a)