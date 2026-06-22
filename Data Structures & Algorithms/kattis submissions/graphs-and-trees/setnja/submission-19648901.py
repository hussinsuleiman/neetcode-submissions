import sys
sys.set_int_max_str_digits(0)

s = input()
res = 1
nb = 1

for c in s:
    if c == 'L':
        res *= 2
    elif c == 'R':
        res = 2*res + nb
    elif c == '*':
        res = 5*res + nb
        nb *= 3

print(res)