n = int(input())
s = input()
res = 0
cups = 0

for i in range(n):
    if s[i] == '1':
        res += 1
        cups = 2
    
    elif cups > 0:
        cups -= 1
        res += 1

print(res)