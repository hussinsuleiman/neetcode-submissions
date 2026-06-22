s = input()
total,i,k = 1,1,1

while i < len(s):
    if ord(s[i]) <= ord(s[i-1]) or k == 6:
        total += 1
        k = 0
    i += 1
    k += 1

print(total)