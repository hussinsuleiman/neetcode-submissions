s = input()
result = [s[0]]
i = 1

while i < len(s):
    while i < len(s) and s[i] == result[-1]:
        i += 1
    
    if i < len(s):
        result.append(s[i])
    
    i += 1

if len(result) < 4:
    print(''.join(result))
    
elif len(result) % 2 == 0:
    print(result[0] + result[1])

else:
    print(result[0] + result[1] + result[2])
    
    

